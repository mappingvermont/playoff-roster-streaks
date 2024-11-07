import pandas as pd
import wikipedia as wp


def get_roster(year):
    if year > 2001:
        page_title = f"{year}_WNBA_Finals"
    else:
        page_title = f"{year}_WNBA_Championship"

    html = wp.page(page_title, auto_suggest=False).html().encode("UTF-8")

    df_list = pd.read_html(html, attrs={"class": "sortable"})

    df_offset = 0

    # if year in [1986, 1985, 1984, 1983, 1981, 1980]:
    #     df_offset = +1

    if year == 2024 or year <= 2010:
        column_offsets = [3, 7]
    else:
        column_offsets = [3, 14]

    # import code
    # code.interact(local=locals())

    df = pd.concat(
        [df_list[df_offset][2:], df_list[df_offset + 1][2:]], ignore_index=True
    ).iloc[:, column_offsets]

    df.columns = ["Name", "From"]
    df["year"] = year

    return df


def main():
    df_list = []

    # for year in range(2024, 1997, -1):
    for year in range(2009, 2001, -1):
        print(year)
        df_list.append(get_roster(year))

    final_df = pd.concat(df_list, ignore_index=True)

    final_df.to_csv("wnba_output.csv", index=False, header=True)


if __name__ == "__main__":
    main()
