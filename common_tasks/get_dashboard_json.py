from other.my_secrets import MySecrets

GIS_5 = MySecrets.get_agol_gis(environment="QA_ENV", user="DBQA_JOHN")

dashboard_json = GIS_5.content.get("7f6ea96949f349e790a04b2eeb1bbe13")
print(dashboard_json)
