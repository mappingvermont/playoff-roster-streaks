import pandas as pd
import wikipedia as wp


def get_roster(year):

    print(year)

    # no tables on wikipedia - pull from local
    if year == 2017:
        return pd.read_csv("src/wnba_2017.csv")

    elif year > 2001:
        page_title = f"{year}_WNBA_Finals"

    else:
        page_title = f"{year}_WNBA_Championship"

    # import code
    # code.interact(local=locals())

    html = wp.page(page_title, auto_suggest=False).html().encode("UTF-8")

    df_list = pd.read_html(html, attrs={"class": "sortable"})

    if year == 2024 or year <= 2010:
        column_offsets = [3, 7]
    else:
        column_offsets = [3, 14]

    df = pd.concat(
        [df_list[0][2:], df_list[1][2:]], ignore_index=True
    ).iloc[:, column_offsets]

    df.columns = ["Name", "From"]
    df["year"] = year

    return df


def main():
    df_list = []

    for year in range(2024, 1996, -1):
        df_list.append(get_roster(year))

    final_df = pd.concat(df_list, ignore_index=True)

    final_df.to_csv("data/wnba.csv", index=False, header=True)


if __name__ == "__main__":
    main()
