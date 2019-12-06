import engine.bin_file as bin_py
import engine.db_structure as db_py
import threading
import os


db = db_py.Database()


def test_binfile():
    test_file = bin_py.BinFile("test.bin")
    test_file.open("w+")
    test_file.write_integer(22, 0, 1)
    test_file.write_bool(False, 1)
    test_file.write_str("vadik", 2, 32)
    test_file.write_float(2.006, 35)
    test_file.write_fixed_integer(877776, 44)
    result_int = test_file.read_integer(0, 1)
    result_bool = test_file.read_bool(1)
    result_str = test_file.read_str(2, 32)
    result_float = test_file.read_float(35)
    result_fixed_int = test_file.read_fixed_integer(44)
    test_file.close()
    os.remove("test.bin")
    assert result_int == 22
    assert not result_bool
    assert result_str == "vadik"
    assert result_float == 2.006
    assert result_fixed_int == 877776


def test_create():
    excepted_table = db_py.Table(db.file)
    excepted_table.name = "vadik_table"
    excepted_table.fields = ["zhenya1", "zhenya2"]
    excepted_table.fields_count = 2
    excepted_table.types = [db_py.Type("int", 4), db_py.Type("str", 256)]
    excepted_table.positions = {"row_id": 1, "zhenya1": 4, "zhenya2": 8}
    excepted_table.row_length = 270
    result_table = db.create_table("vadik_table", 0, {"zhenya1": "int", "zhenya2": "str"})
    assert excepted_table == result_table


def test_show_create():
    fields_names = ["zhenya1", "zhenya2"]
    types_names = ["int", "str"]
    fields = [
        "'" + v + "' " + types_names[i]
        for i, v in enumerate(fields_names)
    ]
    table_name = "vadik_table"
    excepted_string = "--------------------------------------------------------\n"
    excepted_string += "Create table: \n"
    excepted_string += "CREATE TABLE '" + table_name + "' ("
    excepted_string += ", ".join(fields) + ")\n"
    excepted_string += "--------------------------------------------------------"
    result_string = db.tables[0].show_create()
    assert result_string == excepted_string


# Эти функции для тестов, помогают мне получить состояние всей таблицы. При нормальной работе СУБД,
# логика будет бегать по блокам и строчкам с помощью iter_blocks / iter_rows.
def get_block_rows(block):
    rows_list = []
    for row in block.iter_rows():
        rows_list.append(row)
    return rows_list


def get_all_rows_list():
    all_rows_list = []
    for block in db.tables[0].iter_blocks():
        all_rows_list.append(get_block_rows(block))
    return all_rows_list


def test_insert():
    db.tables[0].insert(["zhenya2"], ["test_string_123"])
    db.tables[0].insert(["zhenya1", "zhenya2"], [99, "test_string_123"])
    rows_list = get_all_rows_list()
    assert len(rows_list) == 1
    assert len(rows_list[0]) == 2


def test_delete():
    rows_list = get_all_rows_list()
    db.tables[0].delete([rows_list[0][0].index_in_file])
    rows_list = get_all_rows_list()
    assert len(rows_list[0]) == 1
    db.tables[0].delete()
    rows_list = get_all_rows_list()
    assert len(rows_list[0]) == 0


def test_update():
    db.tables[0].insert(["zhenya1", "zhenya2"], [99, "test_string_123"])
    rows_list = get_all_rows_list()
    assert rows_list[0][0].fields_values_dict["zhenya2"] == "test_string_123"
    db.tables[0].update(["zhenya2"], [["lovetsov"]], [rows_list[0][0]])
    rows_list = get_all_rows_list()
    assert rows_list[0][0].fields_values_dict["zhenya1"] == 99
    assert rows_list[0][0].fields_values_dict["zhenya2"] == "lovetsov"


def test_select():
    db.tables[0].insert(["zhenya1", "zhenya2"], [218, "vadik_vadik"])
    db.tables[0].get_rows()
    result_rows_1 = db.tables[0].select(db.tables[0].fields, db.tables[0].rows)
    assert len(result_rows_1) == 2
    result_rows_2 = db.tables[0].select(["zhenya1"], [db.tables[0].rows[1]])
    assert len(result_rows_2) == 1
    assert result_rows_2[0].fields_values_dict["zhenya1"] == 218


def test_transaction():
    id = db.tables[0].start_transaction()
    db.tables[0].update(["zhenya2"], [["lovetsov"]], [db.tables[0].rows[0]], id)
    db.tables[0].update(["zhenya1"], [[98]], [db.tables[0].rows[0]], id)
    db.tables[0].insert(["zhenya1", "zhenya2"], [99, "test_string_123"], transaction_id=id)
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "test_string_321"], transaction_id=id)
    db.tables[0].delete([db.tables[0].rows[-1].index_in_file], id)
    db.tables[0].end_transaction(id)
    db.tables[0].get_rows()
    assert db.tables[0].rows[0].fields_values_dict["zhenya2"] == "lovetsov"
    assert db.tables[0].rows[0].fields_values_dict["zhenya1"] == 98
    assert len(db.tables[0].rows) == 3


def test_read_commited():
    id = db.tables[0].start_transaction()
    db.tables[0].update(["zhenya2"], [["anime"]], [db.tables[0].rows[0]], id)
    result_rows = db.tables[0].select(["zhenya2"], db.tables[0].rows, id)
    result_value = result_rows[0].fields_values_dict["zhenya2"]
    db.tables[0].end_transaction(id)
    assert result_value == "lovetsov"


def test_rollback():
    id = db.tables[0].start_transaction()
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "test_string_321"], transaction_id=id)
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "tesssst_string_321"], transaction_id=id)
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "tesssttttt_string_321"], transaction_id=id)
    db.tables[0].end_transaction(id, True)
    db.tables[0].get_rows()
    assert len(db.tables[0].rows) == 6
    db.tables[0].rollback_transaction(id)
    db.tables[0].get_rows()
    assert len(db.tables[0].rows) == 3


def test_wide_rollback():
    id = db.tables[0].start_transaction()
    db.tables[0].update(["zhenya2"], [["xxx"]], [db.tables[0].rows[0]], id)
    db.tables[0].end_transaction(id, True)
    db.close_db()
    db.connect_to_db("zhavoronkov.vdb")
    db.tables[0].get_rows()
    assert db.tables[0].rows[0].fields_values_dict["zhenya2"] == "anime"
    assert len(db.tables[0].rows) == 3


def test_durability():
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "tesssst_string_321"], test_rollback=True)
    db.close_db()
    db.connect_to_db("zhavoronkov.vdb")
    db.tables[0].get_rows()
    assert len(db.tables[0].rows) == 3


def thread_function():
    id = db.tables[0].start_transaction()
    db.tables[0].update(["zhenya2"], [["mmmm"]], [db.tables[0].rows[2]], id)
    db.tables[0].end_transaction(id)


def test_repeatable_read():
    id = db.tables[0].start_transaction()
    db.tables[0].insert(["zhenya1", "zhenya2"], [228, "greta_sobaka"], transaction_id=id)
    result_rows_one = db.tables[0].select(["zhenya2"], db.tables[0].rows, id)
    result_value_one = result_rows_one[2].fields_values_dict["zhenya2"]
    new_thread = threading.Thread(target=thread_function)
    new_thread.start()
    result_rows_two = db.tables[0].select(["zhenya2"], db.tables[0].rows, id)
    result_value_two = result_rows_two[2].fields_values_dict["zhenya2"]
    db.tables[0].end_transaction(id)
    assert result_value_one == result_value_two
