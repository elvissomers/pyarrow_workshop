import prepare
import analyze
import visualize
import compare_speed

def main():
    table = prepare.get_table('funda_utrecht_v2.arrow')
    table = analyze.add_price_per_m2(table)

    neighbourhoods_by_price_per_m2 = analyze.sort_neighbourhood_by_price(table)
    neighbourhoods_by_plot_size = analyze.sort_neighbourhood_by_plot_size(table)

    visualize.bar_plot_first_10(neighbourhoods_by_price_per_m2, "price_per_m2")
    visualize.bar_plot_first_10(neighbourhoods_by_plot_size, "plot_area")

    compare_speed.compare(10000000, True, 1)
    compare_speed.compare(10000000, False, 2)
    compare_speed.compare(100000000, False, 3)
    compare_speed.compare(1000000000, False, 4)


if __name__ == "__main__":
    main()