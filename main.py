def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
  
    contro = 0
    quanti = 0

    if len(figurinhas_da_maria) < len(figurinhas_do_joao):  
        for i in range(len(figurinhas_da_maria)):
            for j in range(len(figurinhas_do_joao)):
                if figurinhas_da_maria[i] == figurinhas_do_joao[j]:
                    control += 1
        quanti = len(figurinhas_da_maria) - control


    elif len(figurinhas_do_joao) < len(figurinhas_da_maria):
        for i in range(len(figurinhas_do_joao)):
            for j in range(len(figurinhas_da_maria)):
                if figurinhas_do_joao[i] == figurinhas_da_maria[j]:
                    control += 1
        quanti = len(figurinhas_do_joao) - control

                                                              
    else:
        for i in range(len(figurinhas_da_maria)):
            for j in range(len(figurinhas_do_joao)):
                if figurinhas_da_maria[i] == figurinhas_do_joao[j]:
                    control += 1
        quanti = len(figurinhas_da_maria) - control

    return quanti