anonascimentos = 0
anoatual = 0
idade = 0
opcao = 0

puts "Digite 1 para calcular a sua idade usando o ano atual e o ano que nasceu"
puts "Digite 2 para calcular o ano que você nasceu usando a sua idade atual"
puts "Digite qualquer outra coisa para parar o programa"
opcao = gets.chomp.to_i

if opcao == 1
  puts "Que ano você nasceu?"
  anonascimentos = gets.chomp.to_i
  puts "Que ano estamos?"
  anoatual = gets.chomp.to_i
  puts "Você tem #{anoatual - anonascimentos} anos."
elsif opcao == 2
  puts "Qual a sua idade?"
  idade = gets.chomp.to_i
  puts "Em que ano estamos?"
  anoatual = gets.chomp.to_i
  puts "Você nasceu no ano de #{anoatual - idade}."
else
  puts "Programa encerrado."
end