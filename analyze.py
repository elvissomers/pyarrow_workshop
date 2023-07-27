import pyarrow as pa
import pyarrow.compute as pc

def add_price_per_m2(table):
    price_per_m2 = pc.divide(table.column("selling_price"), table.column("floor_area"))
    return table.append_column("price_per_m2", price_per_m2)

def sort_neighbourhood_by_price(table):
    return pa.TableGroupBy(table, "neighbourhood").aggregate([("price_per_m2", "hash_mean")]).sort_by("price_per_m2_mean")

def sort_neighbourhood_by_plot_size(table):
    return pa.TableGroupBy(table, "neighbourhood").aggregate([("plot_area", "hash_mean")]).sort_by([("plot_area_mean", "descending")])