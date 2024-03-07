def verificar_forca_senha(senha):


  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

  # TODO: Verifique se a senha contém letras maiúsculas e minúsculas
  letras_maiusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  for letra in letras_maiusculas:
    if letra in senha:
      tem_letra_maiuscula = True
    elif letra.lower() in senha:
      tem_letra_minuscula = True
    
  
  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."

  # TODO: Verificar o comprimento mínimo e critérios de validação
  numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  for num in numeros:
    if num in senha:
      tem_numero = True
      
  especial = ['~','!','@','#','$','%','^','&','*','(',')','-','+','/','?','>','<','/','|','=']
  for esp in especial:
    if esp in senha:
      tem_caractere_especial = True
  
  if tem_caractere_especial and tem_letra_maiuscula and tem_letra_minuscula and tem_numero:
    return "Sua senha atende aos requisitos de seguranca. Parabens!"  
  else:
    return "Sua senha nao atende aos requisitos de seguranca."


# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)