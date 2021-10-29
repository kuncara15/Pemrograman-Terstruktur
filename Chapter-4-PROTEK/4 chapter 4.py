kotaA_keB = 125
kecepatanKotaA_keB = 62
kotaB_keC = 256
kecepatanKotaB_keC = 70

waktuJamKotaA_keB   = kotaA_keB // kecepatanKotaA_keB
waktuMenitKotaA_keB = round((kotaA_keB % kecepatanKotaA_keB) / kecepatanKotaA_keB * 60)
waktuJamkotaB_keC = kotaB_keC // kecepatanKotaB_keC
waktuMenitKotaB_keC = round((kotaB_keC % kecepatanKotaB_keC) / kecepatanKotaB_keC * 60)

waktuJamBerangkat   = 6
waktuMenitBerangkat = 0
waktuMenitRehat = 45

waktuJamSampai   = (waktuJamBerangkat + waktuJamKotaA_keB + waktuJamkotaB_keC)
waktuMenitSampai = (waktuMenitBerangkat + waktuMenitKotaA_keB + waktuMenitKotaB_keC + waktuMenitRehat)
if (waktuMenitSampai >= 60):
	waktuJamSampai += 1
	waktuMenitSampai -= 60

	
print("Waktu sampai yaitu %d.%d" % (waktuJamSampai,waktuMenitSampai))
