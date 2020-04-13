# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:19:05 2020

@author: intel
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as BS



options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path = "C:/Users/intel/chromedriver/driver/chromedriver.exe", options = options)
driver.get('https://www.builtwith.com/login')
print("Going...")
driver.implicitly_wait(5)
eid =  driver.find_element_by_id("email")
eid.send_keys("nikhilsunil90s@gmail.com")#Apni id here
pid = driver.find_element_by_id("password")
#print("Going...")
driver.implicitly_wait(2)
pid.send_keys("premlata@321")#Apna password here
print("Going...")
driver.implicitly_wait(5)
b = driver.find_element_by_class_name('btn')
b.click()
print("Going...")
driver.implicitly_wait(5)

linklist = [
 'agapelive.com',
 'ageofaquaria.com',
 'agiftpersonalized.com',
 'agilitegear.com',
 'agron.io',
 'ahlemeyewear.com',
 'ahuva.com',
 'aidabicaj.com',
 'aimeecherieintimates.com',
 'aintnobodycool.com',
 'airfrypan.com',
 'airgunopticsplus.com',
 'airobrands.com',
 'airpaq.de',
 'airplantcity.com',
 'airplantshop.com',
 'airportag.com',
 'airvapeusa.com',
 'ajwallpaper.com',
 'akalean.com',
 'akelasurf.com',
 'aklasu.co',
 'akmetalarts.com',
 'aknology.com',
 'akolaproject.org',
 'akrikks.com',
 'akrithi.com',
 'aksalmonsisters.com',
 'akshuanding.com',
 'akumuink.com',
 'al-farasha.de',
 'alabasterco.com',
 'alacouture.com',
 'alaindupetit.ca',
 'alaindupetit.com',
 'alalastyle.com',
 'alamourthelabel.com',
 'alaninu.com',
 'albaba-sweets.com',
 'albertacrafttours.com',
 'albionfit.com',
 'alchemyjeweler.com',
 'alchitry.com',
 'aldeaprint.com',
 'alderandcoshop.com',
 'aldernewyork.com',
 'alencorp.com',
 'alesift.com',
 'alexanderbattery.com',
 'alexandnia.com.au',
 'alexandriamineral.com',
 'alexandtrahanas.com',
 'alexiaco.com',
 'alexisawesome.com',
 'alexski.com',
 'alfabshop.com',
 'alfawise.com',
 'alfredsapartment.com',
 'aliceandagnes.com',
 'aliceandames.com',
 'aliceandwhittles.com',
 'alienfreshjerky.com',
 'alienoutfitters.com',
 'alifenewyork.com',
 'alifeplus.com.au',
 'alisa.ua',
 'alisamichelle.com',
 'alittleladyshop.com',
 'alittlesomethingvt.com',
 'alkalife.com.au',
 'allanimalgifts.com',
 'allaroundvegan.com',
 'allbirds.com.au',
 'alldock.com.au',
 'alldrinalmonds.com',
 'allegrobeautystore.com',
 'allenarmstactical.com',
 'allevebiotics.com',
 'alleyoop.co.za',
 'allgiftframes.com',
 'allgreatapparel.com',
 'allhempeverything.co.uk',
 'alliedcycleworks.com',
 'allissiasatticdesign.com.au',
 'allithypermarket.com.my',
 'alljigsawpuzzles.co.uk',
 'allkindsofeverything.in',
 'allnaturalbullysticks.com',
 'allparts.uk.com',
 'allpartsuktrade.com',
 'allpassportcover.com',
 'allplants.com',
 'allsilvergifts.com',
 'allstarproducts.ca',
 'allswellhome.com',
 'alltheanime.com',
 'alltimers.com',
 'alltoolsnt.com.au',
 'alltrendygifts.com',
 'allurring.com',
 'allvirginhair.com',
 'allwatchbands.com',
 'allweathermotorsports.com',
 'allwoodfurn.com',
 'allworldfurniture.com',
 'allysonsplace.com',
 'almas.pk',
 'almightyjerseys.com',
 'almondclear.com',
 'almondsurfboards.com',
 'aloha.com',
 'alohafunwear.com',
 'alorstore.com',
 'aloyoga.com',
 'alpacadirect.com',
 'alpen-glass.com',
 'alpha-grooming.com',
 'alphadog.it',
 'alphadognutrition.com',
 'alphagripz.com',
 'alphakillaz.com',
 'alphalete.eu',
 'alphaleteathletics.com',
 'alphaomegahobby.com',
 'alphaoutpost.com',
 'alpinehemp.com',
 'alpineoutdoorstore.com',
 'alpineslimes.net',
 'alpinestartfoods.com',
 'alrugaibfurniture.com',
 'altanovabranding.com',
 'altarpdx.com',
 'altcos.com',
 'altenew.com',
 'alterreny.com',
 'altiplanoinsulation.com',
 'altitude-sports.com',
 'altitudefitnessoutlet.com',
 'altodiversi.com',
 'aluminatiguitars.com',
 'alwaysfits.com',
 'alwaystimeless.com',
 'alxcouture.com',
 'alynndesigns.com',
 'alyxstudio.com',
 'amabrush.com',
 'amamedicalproducts.com.au',
 'amandauprichard.com',
 'amandine-beaulieu.com',
 'amaratulum.co',
 'amarilojewelry.com',
 'amaryllisapparel.com',
 'amasszodiac.com',
 'amaz1ngstuff.com',
 'amaze-brand.com',
 'amazingbe.com',
 'amazingcosmetics.com',
 'amazingminisales.com',
 'amazonias.net',
 'ambassadher.com',
 'ambrosianutraceuticals.com',
 'americanbarbell.com',
 'americanbuttonmachines.com',
 'americanheritagebullion.com',
 'americanprecisionarms.com',
 'americanracingheaders.com',
 'americanrag.com',
 'americanreserveshop.com',
 'americansunglass.com',
 'americantrench.com',
 'ameridroid.com',
 'ameriglo.com',
 'amishtables.com',
 'amkhaseed.com',
 'amlagreen.com',
 'ammofast.com',
 'ammoniasport.com',
 'amnaughty.in',
 'amokequipment.com',
 'amorbeauty.co',
 'amoretti.com',
 'amourvert.com',
 'ampedandco.com',
 'amplehills.com',
 'amplemeal.com',
 'ampm.in',
 'amrapplusone.com',
 'anacapacoffee.com',
 'anacapaequipment.com',
 'analoguewonderland.co.uk',
 'analogwatchco.com',
 'analuisa.com',
 'anantastones.com',
 'anatomie.com',
 'anaum.ae',
 'anchorheadcoffee.com',
 'andaboveallhealth.com',
 'andareluggage.com',
 'andarwallets.com',
 'andersoncomposites.com',
 'andersonsthemesanddreams.co.uk',
 'andisway.com',
 'andrea.is',
 'andreaiyamah.com',
 'andrebadi.com',
 'androidtvboxesireland.com',
 'andyfrisella.com',
 'anewall.com',
 'angelacaglia.com',
 'angelaroi.com',
 'angelheartboutique.com',
 'angelina-alvarez.com',
 'angelsshareglass.com',
 'angelusdirect.com',
 'angelusshoepolish.com',
 'angieandash.com',
 'aniise.com',
 'animalbacker.com',
 'animate.shop',
 'animationshowofshows.com',
 'animeheroshop.com',
 'animetee.com',
 'aninebing.com',
 'ankarifloruss.com',
 'annahariri.com',
 'annasui.com',
 'annesisteron.com',
 'annieplansprintables.com',
 'annsfabulousfinds.com',
 'anointedfighternutrition.com',
 'anovos.com',
 'ansonbelt.com',
 'ansoncalder.com',
 'anthonysfla.com',
 'anticuable.com',
 'antidote.la',
 'antidote.us',
 'antidotechoco.com',
 'antlionaudio.com',
 'antstores.com',
 'antsylabs.com',
 'anuevajewelry.com',
 'anvilcustoms.com',
 'any-cast.com',
 'anythingamishandmore.com',
 'anythinggreen.com',
 'apatchestore.com',
 'apathy.co',
 'apesnacks.com',
 'apexskiboots.com',
 'apmbodyjewelry.com',
 'apolena.com',
 'apothecanna.com',
 'apothecary87.co.uk',
 'apparel99.com',
 'appleyarns.com',
 'appntd.com',
 'apreciodefabrica.com',
 'apresjewelry.com',
 'aprilistic.com',
 'aprilmichellesweets.com',
 'aputure.com',
 'aquaforestaquarium.com',
 'aqualabaquaria.com',
 'aqualabtechnologies.com',
 'aquariumcoop.com',
 'aquatech.net',
 'aquaticarts.com',
 'aquatiser.com',
 'ar15discounts.com']
#linklist = ['aquatiser.com']
for site in linklist:
    driver.get(f'https://www.builtwith.com/meta/{site}/')
    driver.implicitly_wait(5)
    try:
        metalink = driver.find_element_by_link_text("Meta Data Profile")
    except:
        continue
    else:
        metalink.click()
    driver.implicitly_wait(5)
    soup = BS(driver.page_source,'html5lib')
    body = soup.find('body')
    divs = body.find_all('div' , { 'class' : 'card-body'})
    social_links = []
    addresses = []
    info = {
            'site' : site,
            'addresses' : [],
            'telephones' : [],
            'social_links' : []
            }
    for row in range(len(divs)):
        if row == 0:
            maindl = divs[row].find_all('dl')[1]
            add, tdd = maindl.find_all('dd')
            if add.text:
                addtxt = add.text.lstrip('\n')
                addtxt = add.text.rstrip('\n')
                info['addresses'].append(addtxt)
            if tdd.text:
                tddtxt = tdd.text.lstrip('\n')
                tddtxt = tdd.text.rstrip('\n')
                info['telephones'].append(tddtxt)
        elif row == 3:
            links = []
            for link in divs[row].find_all('a'):
                info['social_links'].append(link.get('href'))
        else:
            continue
    driver.implicitly_wait(10)
    with open('infofile.txt' , 'a' , encoding = "utf-8") as file:
        file.write(str(info) + '\n')
    driver.implicitly_wait(50)






    
                        
                        
                        









