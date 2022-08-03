# codigo de media de alunos

media = float(input("Digite o media final do aluno: "))
frequencia = float(input("Digite a frequencia do aluno: "))

if media >= 6:
  if frequencia >= 75:
    print("aluno aprovado")
  else:
    print("Aluno reprovado por frequencia")
else:
  print("Aluno reprovado por nota")