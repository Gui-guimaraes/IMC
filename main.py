peso = input('Digite seu peso\n')
altura = input('Digite sua altura\n')

peso = float(peso)
altura = float(altura)

if altura >= 10 :
  altura = altura/100

imc = peso / altura ** 2
imc = round(imc, 2)

if imc < 18.5 :
  print('Magreza')
elif imc >= 18.5 and imc < 25 :
  print('Normal')
elif imc >= 25 and imc < 30 :
  print('Sobrepeso')
elif imc >= 30 and imc < 35 :
  print('Obesidade')
elif imc >= 35 and imc < 40 :
  print('Obesidade grau 2')
else :
  print('Obesidade grau 3')
print('IMC:',imc)
print('Fim') 