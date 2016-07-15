with pd.HDFStore("all_data.h5") as writer:
    global_co2.to_hdf(writer, "/greenhouse_gas/global_co2")
