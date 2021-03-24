from other.my_secrets import MySecrets

GIS_1 = MySecrets.get_agol_gis(environment="PROD_ENV", user="DBQA_ADMIN")
# GIS_2 = MySecrets.get_agol_gis(environment="DEV_ENV", user="DBQA_REGRESSION")
# GIS_3 = MySecrets.get_agol_gis(environment="DEV_ENV", user="DBQA_ADMIN")
# GIS_4 = MySecrets.get_agol_gis(environment="DEV_ENV", user="NITRO_ADMIN")
GIS_5 = MySecrets.get_agol_gis(environment="DEV_ENV", user="DBQA_JOHN")
# GIS_6 = MySecrets.get_agol_gis(environment="DEV_ENV", user="DBQA_PUBLISHER")
# GIS = MySecrets.get_agol_gis("DEV_ENV", "DBQA_AUTOMATION")
# BUILT_IN_GIS = MySecrets.get_portal_gis(environment="BUILT-IN_ENV", user="CREATOR")
# MY_PORTAL = MySecrets.get_portal_gis(environment="MY_PORTAL", user="ENT_REGRESSION")
TARGET_FOLDER = "_Cloned"

# Clone an item
item = GIS_1.content.get("f313df46ad554819b88282a1ecd1f4d1")
GIS_5.content.clone_items(items=[item], folder=TARGET_FOLDER)

# Clone a List of Items
# itemids = [
#     "db4339dc5ce74597a548556b01fab89b",
#     "bc8f6840e7cc43a5ae2535f3e4a1846a",
#     "6c29997c5f5c4449963e03d7752d9448",
#     "4ad976a36273498f8b66dc0aad53b74c",
# ]
# items = [GIS_2.content.get(itemid) for itemid in itemids]
# GIS_2.content.clone_items(items=items, folder=TARGET_FOLDER)

# Clone a group
# clone_funcs.clone_group_to_folder(
#     source_group_id="bd43716d950c4aba9b6728750f97b6ca",
#     target_folder=TARGET_FOLDER,
#     source_gis_obj=GIS,
#     target_gis_obj=GIS,
#     copy_data=False,
#     item_types=["Web Map"],
# )

# Clone a folder
# clone_funcs.clone_folder(
#     "Sharing_Options_Dashboards_Edge_Cases",
#     "Sharing_Options_Dashboards_Edge_Cases",
#     GIS_2,
#     GIS_4,
# )
