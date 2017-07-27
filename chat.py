import aiml

print("\nConectando-se ao sistema local...");
print("\n!!!!!!!!!!  !!!!!!!!!!  !!!   !!  !!!   !!  !!!!!!!!!!\n    !!      !!      !!  !!!!  !!  !!!!  !!  !!      !!\n    !!      !!      !!  !! !! !!  !! !! !!  !!      !!\n    !!      !!!!!!!!!!  !!  !!!!  !!  !!!!  !!!!!!!!!!\n    !!      !!      !!  !!   !!!  !!   !!!  !!      !!\n!!!!!!!!!!  !!      !!  !!    !!  !!    !!  !!      !!\n");
print("\nSenhor, por favor digite o protocolo de usuario para eu lhe identificar e liberar o seu acesso.\n"); 

kernel = aiml.Kernel()
kernel.learn('file.aiml')
while True:
    print(kernel.respond(raw_input("_>")))


								 
