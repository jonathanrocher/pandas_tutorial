global_co2 = pd.read_table("data/greenhouse_gaz/co2_mm_global.txt", sep='\s+',
                           parse_dates=[[0, 1]], index_col=0)
