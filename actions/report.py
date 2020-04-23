def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River [{river.id}]')

    for forest in arboretum.forests:
        print(f'Forest [{forest.id}]')


    input("\n\nPress any key to continue...")
