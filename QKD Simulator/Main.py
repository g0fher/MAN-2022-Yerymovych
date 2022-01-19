import random 
import time

def percentage(part, whole):
    Percentage = 100 * float(part)/float(whole)
    return str(Percentage) + "%"

main_loop = 1
exit_test_two = 0

print("Hey, я програма, що симулює розподіл ключа за протоколом BB84")
print("Напишіть '666' будь-коли, щоб перезапустити симуляцію")

cont = 1
while main_loop == 1:
	
	eq_num = 70
	negative_amount = 0
	wrong_chance = 0

	while cont == 1:
		amount_passed, key_amount, zero, one, error_amount, error_check_amount, check_amount, eq_passed  = 0, 0, 0, 0, 0, 0, 0, 0
		key_2_ph_len = 0


		bits_amount = int(input("Скількі бітів повинно бути згенеровано?: "))
		#bits_amount = 1000                                                                #input
		if bits_amount == 666:
			#exit_test_two = 1
			break
		if bits_amount < 1:
			negative_amount = 1
			break

		#show = int(input("Показувати всі операції? 0 або 1: "))
		show = 1                                                                          #input

		eve_chance = int(input("Введіть швидкість прослуховування канала Євою у відсотках: "))
		#eve_chance = 60
		if eve_chance == 666:
			#exit_test_two = 1
			break
		if (eve_chance > 100) or (eve_chance < 1):
			wrong_chance = 1
			break


		bob_key=[]
		alice_key=[]

		sec_phase_bob_key = []
		sec_phase_alice_key = []


		delay_enabled = 1                             # DELAY & ДЕКОР

		if delay_enabled == 1:
			delay = 0.2
			print("Ви поставили", bits_amount, "бітів для передачі, зачекайте завершення прорахунку...")
			time.sleep(1.5)
			print("Початок симуляції...")
			time.sleep(.7)
			print("Завантаження результатів...")
			time.sleep(.7)
		else:
			delay=0



		if show == 1:	
			print("Ранд.біт |", "Ранд.базис |", "Поляр.Аліс  |", " Єва |", "Базис.Єви |", "Поляр.Єви |" " Базис.Боба|", "Поляр.Боба |", "Ключ|", "Помилка"  )


		while amount_passed < bits_amount:                                                #Main block


			key_test_alice = 0
			key_test_bob = 0

			sys_random_bit = random.SystemRandom()
			sys_random_basis = random.SystemRandom()
			random_bit = sys_random_bit.randint(0, 1) #Генеруємо випадковий біт
			random_basis = sys_random_basis.randint(0, 1) #Генеруємо базис: нехай 0 - прямолінійний, а 1 - діагональний


			if random_bit == 0: #Вирахувуэмо поляризацію фотона    {
				if random_basis == 0:
					polarization = "  0°"# 🠕"
				if random_basis == 1:
					polarization = " 45°"# ⬈" 
			elif random_bit == 1:
				if random_basis == 0:
					polarization = " 90°"# ➞"
				if random_basis == 1:
					polarization = "135°"# ⬊"

			if random_basis == 0:
				basis="+"
			elif random_basis == 1:
				basis="x"                                          #}


			sys_eve_check = random.SystemRandom() #Генеруємо чи буде Єва перехоплювати фотон
			eve_check = sys_eve_check.randint(0, 100) 
			#eve_check = 0
			#eve_check = 1
			eve_check_test = 0


			if eve_check <= eve_chance: # Блок якщо Єва перехоплює
				eve_check_test = 1
				sys_eve_random_basis = random.SystemRandom() # Генеруэмо випадковий базис Єви
				eve_random_basis = sys_eve_random_basis.randint(0, 1)
				
				sys_eve_random_wrong_basis = random.SystemRandom() # Генеруємо число для розрахунків при неправильному базисі
				eve_random_wrong_basic = sys_eve_random_wrong_basis.randint(0, 1)		

				if eve_random_basis == 0: # Виставляємо значення базиса
					eve_basis="+"
				elif eve_random_basis == 1:
					eve_basis="x"

				if eve_random_basis == random_basis: #При правильному базисі
					eve_polarization = polarization
				if eve_random_basis != random_basis: #При неправильному
					if random_basis == 1:            # Визначаємо рандомну протилежну поляризацію
						if eve_random_wrong_basic == 0:
							eve_polarization = "  0°"# 🠕"
						else:
							eve_polarization = " 90°"# ➞"
					elif random_basis == 0:
						if eve_random_wrong_basic == 1:
							eve_polarization = " 45°"# ⬈" 
						else:
							eve_polarization = "135°"# ⬊"

				sys_bob_random_basis = random.SystemRandom() # Аналогічна операція для Боба при отриманні даних від Єви  {
				bob_random_basis = sys_bob_random_basis.randint(0, 1)
				sys_bob_random_wrong_basis = random.SystemRandom()
				bob_random_wrong_basic = sys_bob_random_wrong_basis.randint(0, 1) 
				if bob_random_basis == 0:
					bob_basis="+"
				elif bob_random_basis == 1:
					bob_basis="x"
				
				if bob_random_basis == eve_random_basis:
					bob_polarization = eve_polarization

				if bob_random_basis != eve_random_basis:
					if eve_random_basis == 1:
						if bob_random_wrong_basic == 0:
							bob_polarization = "  0°"# 🠕"
						else:
							bob_polarization = " 90°"# ➞"
					elif eve_random_basis == 0:
						if bob_random_wrong_basic == 0: #                    !!!! (перевірка)
							bob_polarization = " 45°"# ⬈" 
						else:
							bob_polarization = "135°"# ⬊"                                                              }
				if bob_random_basis == 0:                             # Вираховуємо біт з поляризації та рандомного базиса 
					if bob_polarization == "  0°":# 🠕"
						bob_test_random_bit = 0
					elif bob_polarization == " 90°":
						bob_test_random_bit = 1
				if bob_random_basis == 1:
					if bob_polarization == " 45°":# 🠕"
						bob_test_random_bit = 0
					elif bob_polarization == "135°":
						bob_test_random_bit = 1
				test=0 # Чи попадає біт в ключ
				if bob_random_basis == random_basis:
					test=1
					key_amount = key_amount + 1
					bob_key.append(bob_test_random_bit) 
					alice_key.append(random_bit)
					if bob_test_random_bit == 0: # Підрахунок кількості одиниць та нулів, просто для експерименту
						zero=zero+1
					if bob_test_random_bit == 1:
						one=one+1	
				error = 0 # Чи сходяться біти, видно тільки зі сторони спостерігача. Ніхто всередині симуляції не знає
				if (test == 1) and (bob_test_random_bit != random_bit):
					error = 1
					error_amount = error_amount + 1 



				if show == 1: #Прінт
					print ("   ", random_bit, "        ", basis, "        ", polarization, "        ", "1", "       ", eve_basis, "       ",eve_polarization, end = " ")
					print("     ", " ", bob_basis, "       ", bob_polarization, end = " ")
					if test == 1:
						print("      ", bob_test_random_bit, end = " ")
					else:
						print("        ", end = " ")
					if error == 1:
						print ("    ", "1")
					else:
						print ("    ", " ")

					

			else: #Блок без Єви, аналогічні дії, тільки без перехоплення, напряму.
				sys_bob_random_basis = random.SystemRandom()
				bob_random_basis = sys_bob_random_basis.randint(0, 1)
				sys_bob_random_wrong_basis = random.SystemRandom()
				bob_random_wrong_basic = sys_bob_random_wrong_basis.randint(0, 1) 
				if bob_random_basis == 0:
					bob_basis="+"
				elif bob_random_basis == 1:
					bob_basis="x"
				test=0
				if bob_random_basis == random_basis:
					bob_polarization = polarization
					test=1
					key_amount = key_amount + 1
					bob_key.append(random_bit) 
					alice_key.append(random_bit)
					if random_bit == 0:
						zero=zero+1
					if random_bit == 1:
						one=one+1	
				if bob_random_basis != random_basis:
					if random_basis == 1:
						if bob_random_wrong_basic == 0:
							bob_polarization = "  0°"# 🠕"
						else:
							bob_polarization = " 90°"# ➞"
					elif random_basis == 0:
						if bob_random_wrong_basic == 1:
							bob_polarization = " 45°"# ⬈" 
						else:
							bob_polarization = "135°"# ⬊"
				if show == 1:
					print ("   ", random_bit, "        ", basis, "        ", polarization, "        ", "0", "        ", "          ", end = " ")
					print("       ", "  ", bob_basis, "       ", bob_polarization, end = " ")
					if test == 1:
						print("      ", random_bit, end = " ")
					else:
						print("        ", end = " ")
					print ("    ", " ")
					
			amount_passed = amount_passed + 1


			bit_check = 0 #Перевірка бітів після розподілення. Повинно бути після всього, але тут все по рядково, тому після кожного біта.
			if test == 1:
				sys_test_check = random.SystemRandom()
				test_check = sys_test_check.randint(0, 100) #Шанс
				if test_check <= 50:
					if eve_check_test == 0:
						bit_check = 0
					if eve_check_test == 1:
						if random_bit == bob_test_random_bit:
							bit_check = 0
						else:
							bit_check = 1
					check_amount = check_amount + 1 

				else:
					if eve_check_test == 0:
						sec_phase_bob_key.append(random_bit)
						key_test_bob = 1

					elif eve_check_test == 1:
						sec_phase_bob_key.append(bob_test_random_bit)
						key_test_bob = 1
					key_2_ph_len += 1
					sec_phase_alice_key.append(random_bit)
					key_test_alice = 1

			
			if False:		
				if key_test_alice == 1:
					print ("    ", "a1")
				else:
					print ("    ", " ")

				if key_test_bob == 1:
					print ("    ", "b1")
				else:
					print ("    ", " ")




			error_check_amount = error_check_amount + bit_check #Рахує кількість помилок

			if show == 1:
				time.sleep(delay)
				delay -=0.01
				if delay < 0:
					delay=0


		if (error_amount > 0) and (key_amount > 0):
			precent_error = percentage(error_amount, key_amount)
		else:
			percent_error = 0
		if (error_check_amount > 0) and (check_amount > 0):
			percent_check_error = percentage(error_check_amount, check_amount)
		else:
			percent_check_error = 0

		if delay_enabled == 1:
			time.sleep(.2)

		print("Довжина ключа після першої фази просіювання: ", key_amount)
		print(" ")

		if delay_enabled == 1:
			time.sleep(.2)

		print("Ключ отриманий Бобом: ", *bob_key, sep="")
		print(" ")

		if delay_enabled == 1:
			time.sleep(.2)	

		print("Ключ згенеровний Алісою: ", *alice_key, sep="")
		print(" ")


		#print("Справжня кількість помилок: ", error_amount)
		#print("Справжній відсоток помилок: ", precent_error)
		#print(zero, one) 


		if delay_enabled == 1:
			time.sleep(.2)

		print("Перевірено та виключено бітів під час другої фази просіювання: ", check_amount)
		print(" ")

		if delay_enabled == 1:
			time.sleep(.2)

		print("Помилок виявлено при перевірці: ", error_check_amount)
		print(" ")

		if delay_enabled == 1:
			time.sleep(.2)

		print("Відсоток помилок виявлено при перевірці: ", percent_check_error) #В розробці
		print(" ")

		if delay_enabled == 1:
			time.sleep(.2)

		print("Ключ після другої фази просіювання алс: ", *sec_phase_alice_key, sep="")
		print(" ")

		if delay_enabled == 1:
			time.sleep(.2)
		print("Ключ після другої фази просіювання боб: ", *sec_phase_bob_key, sep="")
		print(" ")

		if delay_enabled == 1:
			time.sleep(.2)

		print("Довжина ключа після другої фази просіювання: ", key_2_ph_len)
		print(" ")


		#print("alice: ", *sec_phase_alice_key, sep="")
		#rint("bob:   ", *sec_phase_bob_key, sep="")


		if delay_enabled == 1:
			time.sleep(.2)

		print("Завершення операції... ")
		print(" ")

		if delay_enabled == 1:
			time.sleep(.2)


		if False:
			while eq_num > eq_passed:
				print("=", end = "")
				time.sleep(0.001)
				eq_passed += 1

		print(" ")

		cont = int(input("Запустити симуляцію ще раз? 0 або 1: "))
		if cont == 0:
			main_loop = 0
		#cont=0

	if negative_amount == 1:
		while True:
			main_loop = int(input('Ви ввели неправильну кількість бітів. Перезапустити симуляцію? 0 або 1:'))
			if main_loop == 666:
				exit_test_two = 1
				break
			if (main_loop == 1) or (main_loop == 0):
				break
	elif wrong_chance == 1:
		while True:
			main_loop = int(input('Ви ввели неправильний шанс. Перезапустити симуляцію? 0 або 1:'))
			if main_loop == 666:
				exit_test_two = 1
				break
			if (main_loop == 1) or (main_loop == 0):
				break
	#if exit_test_two == 1:
		#break
input("Настисніть 'Enter', щоб вийти з симуляції")
