import exception
import engine.db_structure as eng


class preprocessor:

    def __init__(self):
        self.table_count = 0
        self.db = eng.Database()
        sign_len = self.db.file.read_integer(0, 1)
        sign_str = self.db.file.read_str(1, sign_len)
        if sign_str != self.db.signature:
            pass

    def is_correct_fields(self, fields):
        temp = {}
        for field in fields:
            if field[0] in temp:
                try:
                    raise exception.DuplicateFields(str(field[0] + " " + field[1]))
                except Exception as ex:
                    print(ex)
                    return [False, temp]
            else:
                temp[field[0]] = field[1]
        return [True, temp]

    def is_fields_exists(self, name, fields):
        if name in fields:
            return [True, name]
        return [False, -1]

    def is_table_exists(self, name):
        result = False
        for i in self.db.tables:
            if i.name == name:
                result = True
        return result

    def get_table_index(self, name):
        for i in range(len(self.db.tables)):
            if name == self.db.tables[i].name:
                return i

    def is_correct_condition(self, name, condition):
        if condition[0] == "":
            return True
        if condition[0] in self.db.tables[self.get_table_index(name)].fields:
            return True
        return False

    def build_fields(self, fields, is_star, table_index):
        fields_temp = []
        if is_star:
            for i in self.db.tables[table_index].fields:
                fields_temp.append(i)
        for i in fields:
            fields_temp.append(i)
        return fields_temp

    def is_correct_values(self, name, values):
        table_index = self.get_table_index(name)
        if len(values) != len(self.db.tables[table_index].fields):
            return [False, values]
        for i in range(len(values)):
            if self.db.tables[table_index].types[i].name == "int":
                try:
                    values[i] = int(values[i])
                except:
                    return [False, values]
            if self.db.tables[table_index].types[i].name == "bool":
                if values[i] == "False":
                    values[i] = False
                elif values[i] == "True":
                    values[i] = True
                else:
                    return [False, values]
        return [True, values]

    def create_table(self, name, fields):
        temp = self.is_correct_fields(fields)
        if self.is_table_exists(name):
            try:
                raise exception.TableAlreadyExists(name)
            except Exception as ex:
                print(ex)
        elif temp[0]:
            self.db.create_table(name, self.table_count, temp[1])
            self.table_count += 1

    def show_create_table(self, name):
        if not self.is_table_exists(name):
            try:
                raise exception.TableNotExists(name)
            except Exception as ex:
                print(ex)
        else:
            for i in self.db.tables:
                if i.name == name:
                    print(i.show_create())

    def drop_table(self, name):
        if not self.is_table_exists(name):
            try:
                raise exception.TableNotExists(name)
            except Exception as ex:
                print(ex)
        else:
            pass

    def select(self, name, fields, is_star, condition):
        if not self.is_table_exists(name):
            try:
                raise exception.TableNotExists(name)
            except Exception as ex:
                print(ex)
        elif not self.is_fields_exists(name, fields):
            try:
                raise exception.FieldNotExists(is_fields_exists(name, fields))
            except Exception as ex:
                print(ex)
        elif not self.is_correct_condition(name, condition):
            try:
                raise exception.FieldNotExists(is_fields_exists(name, fields))
            except Exception as ex:
                print(ex)
        else:
            table_index = self.get_table_index(name)
            if condition[0] == "":
                self.db.tables[table_index].get_rows()
                rows = self.db.tables[table_index].rows
            else:
                rows = []
                for i in self.db.tables[table_index].rows:
                    if i.fields_values_dict[condition[0]] == condition[1]:
                        rows.append(i)
            fields = self.build_fields(fields, is_star, table_index)
            rows = self.db.tables[table_index].select(fields, rows)
            result = "| "
            for field in self.db.tables[table_index].fields:
                result += field + " | "
            result += "\n"
            for row in rows:
                result += "| "
                for field in row.fields_values_dict:
                    result += str(row.fields_values_dict[field]) + " | "
                result += "\n"
            print(result)



    def insert(self, name, fields, values):
        temp_correct_values = self.is_correct_values(name, values)
        if not self.is_table_exists(name):
            try:
                raise exception.TableNotExists(name)
            except Exception as ex:
                print(ex)
        elif not self.is_fields_exists(name, fields):
            try:
                raise exception.FieldNotExists(is_fields_exists(name, fields))
            except Exception as ex:
                print(ex)
        elif not temp_correct_values[0]:
            try:
                raise exception.InvalidDataType()
            except Exception as ex:
                print(ex)
        else:
            table_index = self.get_table_index(name)
            if len(fields) == 0:
                for i in range(len(values)):
                    fields.append(self.db.tables[table_index].fields[i])
            self.db.tables[table_index].insert(fields, temp_correct_values[1])

    def update(self, name, fields, values, condition):
        if not self.is_table_exists(name):
            try:
                raise exception.TableNotExists(name)
            except Exception as ex:
                print(ex)
        elif not self.is_fields_exists(name, fields):
            try:
                raise exception.FieldNotExists(is_fields_exists(name, fields))
            except Exception as ex:
                print(ex)
        elif not self.is_correct_values(name, values):
            try:
                raise exception.InvalidDataType()
            except Exception as ex:
                print(ex)
        elif self.is_correct_condition(name, condition):
            try:
                raise exception.FieldNotExists(is_fields_exists(name, fields))
            except Exception as ex:
                print(ex)
        else:
            pass  # update in ENGINE

    def delete(self, name, condition):
        if not self.is_table_exists(name):
            try:
                raise exception.TableNotExists(name)
            except Exception as ex:
                print(ex)
        elif self.is_correct_condition(name, condition):
            try:
                raise exception.FieldNotExists(is_fields_exists(name, fields))
            except Exception as ex:
                print(ex)
        else:
            pass  # delete in ENGINE
