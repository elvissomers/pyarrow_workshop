import pyarrow as pa

def split_postal_code(table):
    df = table.to_pandas()
    df[['postal_digits', 'postal_letters']] = df['postal_code'].str.extract('(\d{4})(\D{2})')
    df = df.drop(columns= 'postal_code')
    return pa.Table.from_pandas(df)

def remove_data_without_floor_area(table):
    df = table.to_pandas()
    df = df[df['floor_area'].notna() & (df['floor_area'] != 0)]
    return pa.Table.from_pandas(df)

def get_table(filename):
    table = pa.ipc.open_file(filename).read_all()
    table = split_postal_code(table)
    return remove_data_without_floor_area(table)