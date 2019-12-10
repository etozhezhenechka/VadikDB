import engine.db_structure as db_py
import os

if os.path.isfile("zhavoronkov.vdb"):
    os.remove("zhavoronkov.vdb")

db = db_py.Database()
db.create_table("vadik_table", 0, {"zhenya1": "int", "zhenya2": "str"})


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


def test_transaction():
    id = db.tables[0].start_transaction()
    db.tables[0].insert(["zhenya1", "zhenya2"], [99, "test_string_123"], transaction_id=id)
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "test_string_321"], transaction_id=id)
    rows_list = get_all_rows_list()
    db.tables[0].update(["zhenya2"], [["lovetsov"]], [rows_list[0][0]])
    db.tables[0].delete([rows_list[0][1].index_in_file])
    db.tables[0].end_transaction(id)
    rows_list = get_all_rows_list()
    assert len(rows_list[0]) == 1
    assert rows_list[0][0].fields_values_dict["zhenya2"] == "lovetsov"


def test_read_commited():
    id = db.tables[0].start_transaction()
    rows_list = get_all_rows_list()
    db.tables[0].update(["zhenya2"], [["anime"]], [rows_list[0][0]], id)
    result_rows = db.tables[0].select(["zhenya2"], [rows_list[0][0]], id)
    db.tables[0].end_transaction(id)
    result_value = result_rows[0].fields_values_dict["zhenya2"]
    assert result_value == "lovetsov"


def test_rollback():
    id = db.tables[0].start_transaction()
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "test_string_321"], transaction_id=id)
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "tesssst_string_321"], transaction_id=id)
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "tesssttttt_string_321"], transaction_id=id)
    db.tables[0].end_transaction(id, True)
    db.tables[0].rollback_transaction(id)
    rows_list = get_all_rows_list()
    assert len(rows_list[0]) == 1
    assert rows_list[0][0].fields_values_dict["zhenya2"] == "anime"


def test_wide_rollback():
    id = db.tables[0].start_transaction()
    rows_list = get_all_rows_list()
    db.tables[0].update(["zhenya2"], [["xxx"]], [rows_list[0][0]], id)
    db.tables[0].end_transaction(id, True)
    db.close_db()
    db.connect_to_db("zhavoronkov.vdb")
    rows_list = get_all_rows_list()
    assert rows_list[0][0].fields_values_dict["zhenya2"] == "anime"


def test_durability():
    db.tables[0].insert(["zhenya1", "zhenya2"], [992, "tesssst_string_321"], test_rollback=True)
    db.close_db()
    db.connect_to_db("zhavoronkov.vdb")
    rows_list = get_all_rows_list()
    assert len(rows_list[0]) == 1
