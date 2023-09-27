from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as kick_user
from django.views.decorators.cache import cache_control
from gaminghubwebsiteapp.models import your_profile
from gaminghubwebsiteapp.models import otp_verify, image_mod, game_scheduler, Contact
from .form import Image_model
import random, datetime
from django.core.mail import send_mail
from twilio.rest import Client

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
today_time = str(hour) + ':' + str(minute) + ':' + str(second)
validate_time = str(hour) + ':' + str(int(minute) + 1) + ':' + str(second)

def loguser(request):
	if request.method == 'POST':
		email = request.POST['email']	
		uname = request.POST['uname']	 
		password = request.POST['password']	 
		cpassword = request.POST['cpassword']	
		profile = request.POST['pp']
		fname = request.POST['fname']
		city = request.POST['city']		
		state = request.POST['state']
		title = request.POST['title']		
		date_birth = request.POST['date_birth']
		country = request.POST['country']
		phone = request.POST['phone']
		if email == '':
			messages.error(request, "Email can not be empty")
			return redirect('/register')
		elif uname == '':
			messages.error(request, "Username can not be empty")
			return redirect('/register')
		elif password == '':
			messages.error(request, "Password can not be empty")
			return redirect('/register')
		elif cpassword == '':
			messages.error(request, "Confirm Password can not be empty")
			return redirect('/register')
		elif profile == '':
			messages.error(request, "Profile photo can not be empty")
			return redirect('/register')
		elif phone == '':
			messages.error(request, "Phone can not be empty")
			return redirect('/register')
		elif state == '':
			messages.error(request, "State can not be empty")
			return redirect('/register')
		elif city == '':
			messages.error(request, "City can not be empty")
			return redirect('/register')
		elif title == '':
			messages.error(request, "Title can not be empty")
			return redirect('/register')
		elif date_birth == '':
			messages.error(request, "Date_of_Birth can not be empty")
			return redirect('/register')
		elif fname == '':
			messages.error(request, "Full Name can not be empty")
			return redirect('/register')
		elif country == '':
			messages.error(request, "Country can not be empty")
			return redirect('/register')
		elif cpassword != password:
			messages.error(request, "Confirm password does not match")
			return redirect('/register')
		else:
			myuser = User.objects.create_user(username=uname, email=email, password=password)
			myuser.save()
			mydetails = your_profile.objects.create(name=uname, state=state, city=city, full_name=fname, title=title, date_birth=date_birth,con=country, phone=phone)
			mydetails.save()
			# form = Image_model(data=request.POST, files=request.FILES)
			# if form.is_valid():
			# 	form.save()
			# 	obj = form.instance
			# 	pass
			while True:
				otp_code = random.randint(100000, 999999)
				break
			in_otp = otp_verify.objects.create(name=uname, otp=otp_code, registered_time=today_time)
			in_otp.save()
			otp_data = otp_verify.objects.filter(name=uname)
			for i in otp_data:
				break
			msg = "Hi " + fname +  " welcome to gamingHUB. Your account verification One Time Password is:-" + str(otp_code)
			send_mail("Thanks for registering", msg,"gamers.gamingHUBofficial@gmail.com", [email], fail_silently=False)
			account_sid = 'AC82323b197171e2a2f12155feb14e4893'
			auth_token = '42381c524d6fcdc0c2d418def28fa207'
			client = Client(account_sid, auth_token)
			message = client.messages.create(
			  from_='+12562910253',
			  body="Hi gamer welcome to gamingHUB. Your gamingHUB verification code is %s"%otp_code,
			  to="+91%s" %phone,
			)
			messages.success(request, "Registered successfully. Please login securely.")
			messages.success(request, "Verification code had been sent to your email.")
			return redirect('/login')
	

def loginuser(request):
	if request.method == 'POST':
		luname = request.POST['luname']
		characters = "!#$%^&*()_+=\|}{][]';:/.,"
		data_status = your_profile.objects.filter(name=luname)
		for e in data_status:
			break
		lpassword = request.POST['lpassword']
		user = authenticate(request, username=luname, password=lpassword)
		for a in characters:
			if a in luname:
				messages.error(request, "Username cannot contain special characters")
				return redirect('/login')
				break
			if a in lpassword:
				messages.error(request, "Password cannot contain special characters (Hint): Use @ to make a strong password")
				return redirect('/login')
				break
		if luname == '':
			messages.error(request, "Username can not be empty")
			return redirect('/login')
		elif lpassword == '':
			messages.error(request, "Password can not be empty")
			return redirect('/login')
		elif user is not None:
			if e.status == False:
				user_login(request, user)
				return redirect('/verify-email')
			else:
				user_login(request, user)
				return redirect('/dashboard')
		else: 
			messages.error(request, "Invalid username or password")
			return redirect('/login')
def logoutuser(request):
	kick_user(request)
	request.session.flush()
	return redirect('/login')
def verifylink(request):
	if request.method == 'POST':
		link = request.POST['verification-link']
		if link == "sushantchaharisdgsushant":
			messages.success(request, "Link has been successfully verified")
			return redirect('/reset-password')
		else:
			messages.error(request, "Invalid link or link had expired")
			return redirect('/forgot-password')
	else:
		return redirect('/forgot-password')
def verifyotp(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			otp_get = request. POST['otp']
			otp_data = otp_verify.objects.filter(name=request.user.username)
			dat = your_profile.objects.filter(name=request.user.username)
			for b in dat:
				break
			for a in otp_data:
				break	
			if (otp_get == a.otp):
				b.status = True
				b.save()
				a.delete()
				messages.success(request, 'Your gamingHUB account has been verified successfully.')
				print(b.status)
				return redirect('/dashboard')
			else:
				messages.error(request, "Invalid otp or otp had expired.")
				return redirect('/verify-email')
		else:
			return redirect('/verify-email')
	else:
		return redirect('/login')
def home(request):
	return render(request, 'index.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
	if request.user.is_authenticated:
		data = your_profile.objects.filter(name=request.user.username)
		return render(request, 'dashboard.html', {'test' : data})
	else:
		return redirect('/login')
def register(request):
	return render(request, 'register.html')
def login(request):
	return render(request, 'login.html')
def forgotpass(request):
	return render(request, 'forgot-password.html')
def resetpass(request):
	return render(request, 'reset-password.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):
	if request.user.is_authenticated:
		data = your_profile.objects.filter(name=request.user.username)
		return render(request, 'profile.html', {'test' : data})
	else:
		return redirect('/login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def chess(request):
	if request.user.is_authenticated:
		return render(request, 'chess.html')
	else:
		return redirect('/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def verifyemail(request):
	if request.user.is_authenticated:
		uniq_dat = your_profile.objects.filter(name=request.user.username)
		for z in uniq_dat:
			break
		if z.status == False:
			return render(request, 'verify-email.html')
		else:
			return redirect('/dashboard')
	else:
		return redirect('/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def generate_code(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			data_status = your_profile.objects.filter(name=request.user.username)
			for f in data_status:
				break
			while True:
				otp_code = random.randint(100000, 999999)
				break
			otp_verification = otp_verify.objects.filter(name=request.user.username)
			if otp_verify != None:
				for b in otp_verification:
					b.otp = otp_code
					b.save()
					print(b.otp)
					break
			messages.success(request, "Verification code has been sent to your email.")
			msg = "Hi " + f.full_name +  " welcome to gamingHUB. Your account verification One Time Password is:-" + str(otp_code)
			send_mail("Thanks for registering", msg,"gamers.gamingHUBofficial@gmail.com", [request.user.email], fail_silently=False)
			account_sid = 'AC82323b197171e2a2f12155feb14e4893'
			auth_token = '42381c524d6fcdc0c2d418def28fa207'
			client = Client(account_sid, auth_token)
			message = client.messages.create(
			from_='+12562910253',
			body="Hi gamer welcome to gamingHUB. Your gamingHUB verification code is %s"%otp_code,
			to="+91%s" %f.phone,
			)
			return redirect('/verify-email')
		else:
			return redirect('/login')
	else:
		return redirect('/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def game_schedule(request):
	if request.user.is_authenticated:
		if request.method == "GET":
			targetname = request.GET['tn']
			date = request.GET['date']
			game = request.GET['game']
			time = request.GET['time']
			if targetname == '' and date == '':
				messages.error(request, "Target name or date field cannot be empty")
			elif time == '' and game == '':
				messages.error(request, "Time or game field cannot be empty")
			else:
				data_status = your_profile.objects.filter(name=request.user.username)
				for f in data_status:
					break
				schedule_your_game = game_scheduler.objects.create(name = request.user.username, email= request.user.email, phone=f.phone, target_name = targetname, schedule_date=date, schedule_time=time, game=game)
				schedule_your_game.save()
				game_schedule = game_scheduler.objects.filter(name=request.user.username)
				for n in game_schedule:
					break
				account_sid = 'AC82323b197171e2a2f12155feb14e4893'
				auth_token = '42381c524d6fcdc0c2d418def28fa207'
				client = Client(account_sid, auth_token)
				message = client.messages.create(
				from_='+12562910253',
				body="Hi gamer welcome to gamingHUB. gamingHUB is a online platform which provides your free gaming service without downloading on your system. You had set a target",
				to="+91%s" %f.phone,
				)
				call = client.calls.create(
					url='http://demo.twilio.com/docs/voice.xml',
			  		to="+91%s" %f.phone,
					from_='+12562910253',
				)
				msg = "Your game has been successfully scheduled on", date, "at", time
				messages.success(request, msg)
				return redirect('/dashboard')
	else:
		return redirect('/login')

def contact_back(request):
	if request.method == "GET":
		f_n = request.GET['f_n']
		l_n = request.GET['l_n']
		email = request.GET['email']
		phone = request.GET['phone']
		msg = request.GET['msg']

		contact_us = Contact.objects.create(first_name=f_n, last_name=l_n, email_address=email, phone_number=phone,message=msg)
		contact_us.save()
		messages.success(request, "Thanks for sending a message. We shall reply very soon.Best of luck.")
		return redirect('/')
	else:
		return HttpResponse("Error")
