# Hlavní sál divadla má k dispozici 350 sedaček.
# Lze je poskládat do řad po 32 sedadlech tak, aby všechny řady byly úplné?
# Pokud ne, kolik sedaček musíme přikoupit, aby to šlo?
# Kolik nám takto vznikne celkem řad?

zbyva = 350 % 32
dokoupit = 32 - zbyva
celkem_rad = (350 + dokoupit) / 32

#################
# Alternativa
pocet_sedacek_v_cele_rade = 32
pocet_sedacek_k_dispozici = 350

# zbytek po deleni
kolik_prebyva_sedacek = pocet_sedacek_k_dispozici % pocet_sedacek_v_cele_rade

# kolik mi zbyva sedacek do plne rady
pocet_sedacek_k_dokoupeni = pocet_sedacek_v_cele_rade - kolik_prebyva_sedacek

celkovy_pocet_rad = (
    pocet_sedacek_k_dispozici + sedacky_k_dokoupeni
) / pocet_sedacek_v_cele_rade
