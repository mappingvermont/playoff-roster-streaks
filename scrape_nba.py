import pandas as pd
import wikipedia as wp


def get_roster(year):
    html = wp.page(f"{year}_NBA_Finals", auto_suggest=False).html().encode("UTF-8")

    df_list = pd.read_html(html, attrs={"class": "toccolours"})

    df_offset = 0

    if year in [1986, 1985, 1984, 1983, 1981, 1980]:
        df_offset = +1

    df = pd.concat([df_list[df_offset][2:], df_list[df_offset + 1][2:]], ignore_index=True).iloc[:, [2, 6]]

    df.columns = ["player", "college"]
    df["year"] = year

    return df


def main():

    df_list = []

    for year in range(2024, 1979, -1):
        print(year)
        df_list.append(get_roster(year))

    final_df = pd.concat(df_list, ignore_index=True)

    final_df.to_csv("data/nba.csv", index=False, header=True)


if __name__ == "__main__":
    main()
