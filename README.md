# CanalPlusSport-

To run the scraper the `api_url = "https://secure-webtv-static.canal-plus.com/metadata/cpfra/all/v2.2/globalchannels.json"`
To print to the `CSV` The `tv_programme` to get the channels `print("\n".join(sorted(list(tv_programme.keys()))))`

That will give you the below except all the channels:
`MULTISPORTS 1 MULTISPORTS 2 MULTISPORTS 3 MULTISPORTS 4 MULTISPORTS 5 MULTISPORTS 6`

Printing to the `csv` the

`df = pd.DataFrame(tv_programme["MULTISPORTS 1"], columns=["Title", "Subtitle", "Time", ]) df.to_csv("MULTISPORTS1.csv", index=False)`

The output in the `csv` will be:

`
Title Subtitle Time

---

Basket-ball - Nanterre / Bursa 5e journée. Groupe D 17:00
Premier League World Mag Foot 19:00
Pépite RMC Sport Doc Sport 19:30
Basket-ball - Villeurbanne / CSKA Moscou 16e journée 19:45
PL Zone Mag Foot 21:45
Premier League World Mag Foot 22:45
Transversales Mag Foot 23:15
Transversales Mag Foot 00:45
Transversales Mag Foot 02:00
`
