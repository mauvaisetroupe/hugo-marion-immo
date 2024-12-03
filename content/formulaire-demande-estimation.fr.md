---
title: "Formulaire Demande Estimation"
description: "Formulaire de demande d'estimation gratuite de vote maison ou votre appartement à Luxembourg"
images: ["images/P1000780-site.jpg"]
draft: false
menu: 
weight: 
---

{{< rawhtml >}}
<script src="/js/jquery.min.js"></script>


<form action="../php/result.php"  method="POST" accept-charset="UTF-8" class="contact__form" id="contactForm">

            <!-- Name -->
            <div class="contact__field">
                <label for="Nom">Nom : </label>
                <input type="text" name="Nom" placeholder="Votre nom"
                    class="contact__form__input contact__form__name" id="nom"
                    aria-labelledby="nom" required>
            </div>

            <!-- Email -->
            <div class="contact__field">
                <label for="Email">Email</label>
                <input type="email" name="Email" placeholder="Email"
                    class="contact__form__input contact__form__email" id="email"
                    aria-labelledby="email" required>
            </div>
			
			
			<div class="contact__field">
				<label for="address">Ville</label>
				<input list="city" required>
				<datalist id="city">
					<option value="Abweiler">
					<option value="Ahn">
					<option value="Allerborn">
					<option value="Alscheid">
					<option value="Altlinster">
					<option value="Altrier">
					<option value="Altrodeschhof">
					<option value="Altwies">
					<option value="Alzingen">
					<option value="Angelsberg">
					<option value="Ansembourg">
					<option value="Antoniushof">
					<option value="Arsdorf">
					<option value="Aspelt">
					<option value="Assel">
					<option value="Asselborn">
					<option value="Asselscheuer">
					<option value="Banzelt">
					<option value="Basbellain">
					<option value="Bascharage">
					<option value="Baschleiden">
					<option value="Bastendorf">
					<option value="Bavigne">
					<option value="Beaufort">
					<option value="Bech">
					<option value="Bech-Kleinmacher">
					<option value="Beckerich">
					<option value="Beidweiler">
					<option value="Beiler">
					<option value="Belvaux">
					<option value="Berbourg">
					<option value="Berchem">
					<option value="Berdorf">
					<option value="Bereldange">
					<option value="Berg">
					<option value="Bergem">
					<option value="Beringen">
					<option value="Beringerberg">
					<option value="Berlé">
					<option value="Berschbach">
					<option value="Bertrange">
					<option value="Bettange-sur-Mess">
					<option value="Bettborn">
					<option value="Bettel">
					<option value="Bettembourg">
					<option value="Bettendorf">
					<option value="Betzdorf">
					<option value="Beyren">
					<option value="Bigelbach">
					<option value="Bigonville">
					<option value="Bigonville-Poteau">
					<option value="Bilsdorf">
					<option value="Binsfeld">
					<option value="Birkelt">
					<option value="Bissen">
					<option value="Bivange">
					<option value="Bivels">
					<option value="Biwer">
					<option value="Biwerbach (lb)">
					<option value="Biwisch">
					<option value="Blaschette">
					<option value="Blumenthal">
					<option value="Bockholtz">
					<option value="Bockholtz">
					<option value="Boevange">
					<option value="Boevange-sur-Attert">
					<option value="Bofferdange">
					<option value="Bollendorf-Pont">
					<option value="Bonnal">
					<option value="Born">
					<option value="Born-Moulin">
					<option value="Boudler">
					<option value="Boudlerbach">
					<option value="Boulaide">
					<option value="Bour">
					<option value="Bourglinster">
					<option value="Bourscheid">
					<option value="Bourscheid-Moulin (lb)">
					<option value="Bourscheid-Plage">
					<option value="Boursdorf">
					<option value="Bous">
					<option value="Boxhorn">
					<option value="Brachtenbach">
					<option value="Brandenbourg">
					<option value="Brattert">
					<option value="Breidfeld">
					<option value="Breidweiler">
					<option value="Breinert">
					<option value="Bricherhof (lb)">
					<option value="Bridel">
					<option value="Broderbour">
					<option value="Brouch">
					<option value="Brouch">
					<option value="Budersberg">
					<option value="Buderscheid">
					<option value="Burden">
					<option value="Burmerange">
					<option value="Buschdorf">
					<option value="Buschrodt">
					<option value="Calmus">
					<option value="Canach">
					<option value="Cap">
					<option value="Capellen">
					<option value="Carlshof">
					<option value="Christnach">
					<option value="Cinqfontaines">
					<option value="Claushof">
					<option value="Clemency">
					<option value="Clemenshof (lb)">
					<option value="Clervaux">
					<option value="Closdelt (lb)">
					<option value="Colbette">
					<option value="Colmar-Berg">
					<option value="Colpach-Bas">
					<option value="Colpach-Haut">
					<option value="Consdorf">
					<option value="Consthum">
					<option value="Contern">
					<option value="Crauthem">
					<option value="Crendal">
					<option value="Cruchten">
					<option value="Dahl">
					<option value="Dahlem">
					<option value="Dalheim">
					<option value="Deiffelt">
					<option value="Deisermillen">
					<option value="Dellen">
					<option value="Derenbach">
					<option value="Dickweiler">
					<option value="Diekirch">
					<option value="Differdange">
					<option value="Dillingen">
					<option value="Dippach">
					<option value="Dippach-Gare (lb)">
					<option value="Dirbach">
					<option value="Doennange">
					<option value="Doncols">
					<option value="Dondelange">
					<option value="Dorscheid">
					<option value="Drauffelt">
					<option value="Dreiborn">
					<option value="Drinklange">
					<option value="Dudelange">
					<option value="Duderhof">
					<option value="Echternach">
					<option value="Ehlange-sur-Mess">
					<option value="Ehlerange">
					<option value="Ehnen">
					<option value="Ehner">
					<option value="Eischen">
					<option value="Eisenbach">
					<option value="Eisenborn">
					<option value="Ell">
					<option value="Ellange">
					<option value="Eltz (lb)">
					<option value="Elvange">
					<option value="Elvange">
					<option value="Emerange">
					<option value="Emeschbach (lb)">
					<option value="Enscherange">
					<option value="Enteschbach">
					<option value="Eppeldorf">
					<option value="Ermsdorf">
					<option value="Ernster">
					<option value="Ernzen">
					<option value="Erpeldange">
					<option value="Erpeldange">
					<option value="Erpeldange">
					<option value="Ersange">
					<option value="Eschdorf">
					<option value="Eschette">
					<option value="Esch-sur-Alzette">
					<option value="Esch-sur-Sûre">
					<option value="Eschweiler">
					<option value="Eschweiler">
					<option value="Eselborn">
					<option value="Essingen">
					<option value="Ettelbruck">
					<option value="Everlange">
					<option value="Fausermuehle">
					<option value="Fennange">
					<option value="Fentange">
					<option value="Filsdorf">
					<option value="Findel">
					<option value="Fingig">
					<option value="Finsterthal (lb)">
					<option value="Fischbach">
					<option value="Fischbach">
					<option value="Flatzbour (lb)">
					<option value="Flaxweiler">
					<option value="Flebour (Boulaide) (lb)">
					<option value="Flebour (Bourscheid) (lb)">
					<option value="Foetz">
					<option value="Folkendange">
					<option value="Folschette">
					<option value="Fond-de-Gras">
					<option value="Fond de Heiderscheid">
					<option value="Fossenhof (lb)">
					<option value="Fouhren">
					<option value="Freckeisen (lb)">
					<option value="Frohmuehle">
					<option value="Friedbusch (lb)">
					<option value="Friedhof">
					<option value="Frisange">
					<option value="Garnich">
					<option value="Gaichel">
					<option value="Gemenerhof">
					<option value="Geyershof (Bech) (lb)">
					<option value="Geyershof (Parc Hosingen) (lb)">
					<option value="Gilsdorf">
					<option value="Girst">
					<option value="Girsterklaus (lb)">
					<option value="Givenich">
					<option value="Godbrange">
					<option value="Goebelsmuhle">
					<option value="Goeblange">
					<option value="Goedange">
					<option value="Goesdorf">
					<option value="Goetzingen">
					<option value="Gonderange">
					<option value="Gosseldange">
					<option value="Gostingen">
					<option value="Gralingen">
					<option value="Grand-Bevange">
					<option value="Grass">
					<option value="Graulinster">
					<option value="Greisch">
					<option value="Greiveldange">
					<option value="Grevels">
					<option value="Grentzingen">
					<option value="Grevenknapp">
					<option value="Grevenmacher">
					<option value="Grindhausen">
					<option value="Grosbous">
					<option value="Grummelscheid">
					<option value="Grundhof">
					<option value="Hachiville">
					<option value="Hagelsdorf">
					<option value="Hagen">
					<option value="Haller">
					<option value="Hamiville">
					<option value="Harlange">
					<option value="Hassel">
					<option value="Haut-Martelange">
					<option value="Hautbellain">
					<option value="Hautcharage">
					<option value="Heffingen">
					<option value="Heiderscheid">
					<option value="Heinerscheid">
					<option value="Heisdorf">
					<option value="Heispelt">
					<option value="Helfenterbruck (lb)">
					<option value="Hellange">
					<option value="Helmdange">
					<option value="Helmsange">
					<option value="Hemstal">
					<option value="Herborn">
					<option value="Herrenberg">
					<option value="Hersberg">
					<option value="Hesperange">
					<option value="Hettermillen (lb)">
					<option value="Hierheck">
					<option value="Hinkel">
					<option value="Hinterhassel">
					<option value="Hirtzenhof (lb)">
					<option value="Hivange">
					<option value="Hobscheid">
					<option value="Hoesdorf">
					<option value="Hoffelt">
					<option value="Hollenfels">
					<option value="Holler">
					<option value="Holler-Moulin (lb)">
					<option value="Holtz">
					<option value="Holzem">
					<option value="Holzthum">
					<option value="Hoscheid">
					<option value="Hoscheid-Dickt (lb)">
					<option value="Hoscheidterhof (Putscheid) (lb)">
					<option value="Hoscheidterhof (Tandel) (lb)">
					<option value="Hosingen">
					<option value="Hostert">
					<option value="Hostert">
					<option value="Hovelange">
					<option value="Howald">
					<option value="Huldange">
					<option value="Huncherange">
					<option value="Hunsdorf">
					<option value="Hupperdange">
					<option value="Huttange">
					<option value="Imbringen">
					<option value="Ingeldorf">
					<option value="Insenborn">
					<option value="Itzig">
					<option value="Junglinster">
					<option value="Kaaspelterhof (lb)">
					<option value="Kaesfurt">
					<option value="Kahler">
					<option value="Kalborn">
					<option value="Kalkesbach (lb)">
					<option value="Kapenacker">
					<option value="Kapweiler">
					<option value="Kaundorf">
					<option value="Kautenbach">
					<option value="Kayl">
					<option value="Kehlen">
					<option value="Kehmen">
					<option value="Keispelt">
					<option value="Keiwelbach (lb)">
					<option value="Kippenhof (lb)">
					<option value="Kirelshof (lb)">
					<option value="Kleemühle (lb)">
					<option value="Kleinbettingen">
					<option value="Klingelscheuer">
					<option value="Knaphoscheid">
					<option value="Kobenbour">
					<option value="Kuelbécherhaff (lb)">
					<option value="Kockelscheuer">
					<option value="Koedange">
					<option value="Koerich">
					<option value="Koetschette">
					<option value="Kopstal">
					<option value="Kuborn">
					<option value="Lamadelaine">
					<option value="Landscheid">
					<option value="Lannen">
					<option value="Larochette">
					<option value="Lasauvage">
					<option value="Lausdorn">
					<option value="Lauterborn">
					<option value="Leesbach (lb)">
					<option value="Lehrhof (lb)">
					<option value="Leithum">
					<option value="Lellig">
					<option value="Lellingen">
					<option value="Lenningen">
					<option value="Lentzweiler">
					<option value="Leudelange">
					<option value="Levelange">
					<option value="Liefrange">
					<option value="Lieler">
					<option value="Lilien (lb)">
					<option value="Limpach">
					<option value="Linger">
					<option value="Lintgen">
					<option value="Lipperscheid">
					<option value="Livange">
					<option value="Longsdorf">
					<option value="Lorentzweiler">
					<option value="Lullange">
					<option value="Lultzhausen">
					<option value="Luxembourg">
					<option value="Machtum">
					<option value="Mamer">
					<option value="Manternach">
					<option value="Marienthal">
					<option value="Marnach">
					<option value="Marscherwald">
					<option value="Masseler">
					<option value="Maulusmuehle (lb)">
					<option value="Mecher">
					<option value="Mecher">
					<option value="Medernach">
					<option value="Medingen">
					<option value="Meispelt">
					<option value="Mensdorf">
					<option value="Merkholtz">
					<option value="Mersch">
					<option value="Merscheid">
					<option value="Merscheid">
					<option value="Mertert">
					<option value="Mertzig">
					<option value="Meysembourg">
					<option value="Michelau">
					<option value="Michelbouch">
					<option value="Michelshof">
					<option value="Moersdorf">
					<option value="Moesdorf">
					<option value="Moestroff">
					<option value="Mompach">
					<option value="Mondercange">
					<option value="Mondorf-les-Bains">
					<option value="Moutfort">
					<option value="Mullendorf">
					<option value="Mullerthal">
					<option value="Munsbach">
					<option value="Munschecker">
					<option value="Munshausen">
					<option value="Nachtmanderscheid">
					<option value="Nagem">
					<option value="Neidhausen">
					<option value="Neudorf (Luxembourg) (lb)">
					<option value="Neuhäusgen">
					<option value="Neunhausen">
					<option value="Niederanven">
					<option value="Niederdonven">
					<option value="Niederfeulen">
					<option value="Niederglabach (lb)">
					<option value="Niederkorn">
					<option value="Niederpallen">
					<option value="Niederwampach">
					<option value="Nocher">
					<option value="Nocher-Route (lb)">
					<option value="Noerdange">
					<option value="Noertrange">
					<option value="Noertzange">
					<option value="Nommern">
					<option value="Nospelt">
					<option value="Nothum">
					<option value="Oberanven">
					<option value="Oberdonven">
					<option value="Obereisenbach">
					<option value="Oberfeulen">
					<option value="Oberglabach">
					<option value="Oberkorn">
					<option value="Oberpallen">
					<option value="Oberschlinder (lb)">
					<option value="Oberwampach">
					<option value="Openthalt (lb)">
					<option value="Oetrange">
					<option value="Olingen">
					<option value="Olm">
					<option value="Ospern">
					<option value="Osweiler">
					<option value="Peppange">
					<option value="Perlé">
					<option value="Pétange">
					<option value="Petit-Bevange">
					<option value="Petit-Nobressart">
					<option value="Pettingen">
					<option value="Pintsch">
					<option value="Pissange">
					<option value="Platen">
					<option value="Pommerloch">
					<option value="Pontpierre">
					<option value="Pratz">
					<option value="Prettingen">
					<option value="Preizerdaul">
					<option value="Putscheid">
					<option value="Rambrouch">
					<option value="Rameldange">
					<option value="Reckange">
					<option value="Reckange-sur-Mess">
					<option value="Reckingerhof (lb)">
					<option value="Redange">
					<option value="Reichlange">
					<option value="Reimberg">
					<option value="Reisdorf">
					<option value="Remerschen">
					<option value="Remich">
					<option value="Reuland">
					<option value="Reuler">
					<option value="Riesenhof">
					<option value="Rindschleiden">
					<option value="Ringel">
					<option value="Rippig">
					<option value="Rippweiler">
					<option value="Rodange">
					<option value="Rodenbourg">
					<option value="Roder">
					<option value="Rodershausen">
					<option value="Roedgen">
					<option value="Roeser">
					<option value="Roedt (lb)">
					<option value="Rolling">
					<option value="Rollingen">
					<option value="Rombach-Martelange">
					<option value="Roodt">
					<option value="Roodt-sur-Eisch">
					<option value="Roodt-sur-Syre">
					<option value="Roost">
					<option value="Rosport">
					<option value="Rossmühle (lb)">
					<option value="Roullingen">
					<option value="Rumelange">
					<option value="Rumlange">
					<option value="Saeul">
					<option value="Sandweiler">
					<option value="Sanem">
					<option value="Sassel">
					<option value="Savelborn">
					<option value="Schandel">
					<option value="Scheidel">
					<option value="Scheidgen">
					<option value="Schengen">
					<option value="Scheuerberg">
					<option value="Schieren">
					<option value="Schifflange">
					<option value="Schiltzberg (lb)">
					<option value="Schimpach">
					<option value="Schleif (lb)">
					<option value="Schlindermanderscheid">
					<option value="Schmiede (lb)">
					<option value="Schoenfels">
					<option value="Schoos">
					<option value="Schouweiler">
					<option value="Schrassig">
					<option value="Schrondweiler">
					<option value="Schuttrange">
					<option value="Schwebach">
					<option value="Schwebach-Pont (lb)">
					<option value="Schwebsange">
					<option value="Schweich">
					<option value="Schwiedelbrouch">
					<option value="Selscheid">
					<option value="Seltz (Luxembourg) (lb)">
					<option value="Senningen">
					<option value="Senningerberg">
					<option value="Septfontaines">
					<option value="Siebenaler">
					<option value="Simmerfarm (lb)">
					<option value="Simmerschmelz (lb)">
					<option value="Soleuvre">
					<option value="Sonlez">
					<option value="Sprinkange">
					<option value="Stadtbredimus">
					<option value="Staffelstein (lb)">
					<option value="Stegen">
					<option value="Steinfort">
					<option value="Steinheim">
					<option value="Steinsel">
					<option value="Stockem">
					<option value="Stolzembourg">
					<option value="Strassen">
					<option value="Stuppicht (lb)">
					<option value="Surré">
					<option value="Syren">
					<option value="Tadler">
					<option value="Tandel">
					<option value="Tarchamps">
					<option value="Tétange">
					<option value="Tintesmühle (lb)">
					<option value="Trintange">
					<option value="Troine">
					<option value="Troine-Route (lb)">
					<option value="Troisvierges">
					<option value="Tuntange">
					<option value="Uebersyren">
					<option value="Untereisenbach">
					<option value="Unterschlinder (lb)">
					<option value="Urspelt">
					<option value="Useldange">
					<option value="Vianden">
					<option value="Vichten">
					<option value="Wahl">
					<option value="Wahlhausen">
					<option value="Waldbillig">
					<option value="Waldbredimus">
					<option value="Waldhof">
					<option value="Walferdange">
					<option value="Wallendorf-Pont">
					<option value="Walsdorf">
					<option value="Warken">
					<option value="Wasserbillig">
					<option value="Watrange">
					<option value="Wecker">
					<option value="Weicherdange">
					<option value="Weidingen">
					<option value="Weiler">
					<option value="Weilerbach">
					<option value="Weiler-la-Tour">
					<option value="Weiswampach">
					<option value="Welfrange">
					<option value="Wellenstein">
					<option value="Welscheid">
					<option value="Welsdorf">
					<option value="Wemperhardt">
					<option value="Weydig">
					<option value="Weyer (Luxembourg) (lb)">
					<option value="Wickrange">
					<option value="Wiltz">
					<option value="Wilwerdange">
					<option value="Wilwerwiltz">
					<option value="Wincrange">
					<option value="Windhof">
					<option value="Winseler">
					<option value="Wintrange">
					<option value="Wirtgensmuehle (lb)">
					<option value="Wolper (lb)">
					<option value="Wolwelange">
					<option value="Wormeldange">
					<option value="Wormeldange-Haut">
					<option value="Zittig">
				</datalist>
			</div>
			<div class="contact__field">
				<label for="address">Adresse (nom de la rue, quartier)</label>
				<input type="text" id="address" name="address" min="1" max="20" >
			</div>




            <div class="contact__field">
                <label for="description">Quel type de bien souhaitez vous estimer ?</label>
                <div>
				  <input type="radio" id="maison" name="typebien" value="maison" checked>
				  <label for="Maisons">Maison</label>
				</div>
				<div>
				  <input type="radio" id="appartement" name="typebien" value="appartement">
				  <label for="appartement">Appartement</label>
				</div>
				
            </div>
			
			

            <div class="contact__field">
                <label for="surface">Quelle est la surface de votre maison / appartement ?</label>
                <input type="tel" name="surface" placeholder="surface"
                    class="contact__form__input contact__form__surface" id="surface"
                    aria-labelledby="surface" required>
            </div>

            <div class="contact__field">
                <label for="surface-terrain">Quelle est la surface du terrain (pour maison) ?</label>
                <input type="tel" name="surface-terrain" placeholder="surface terrain"
                    class="contact__form__input contact__form__surface" id="surface"
                    aria-labelledby="surface terrain" required>
            </div>
			
			<div class="contact__field">
				<label for="nbpiece">Nombre de pièces(1-20): (cuisine, salle de bain et les toilettes ne sont pas à prendre en compte)</label>
				<input type="number" id="nbpiece" name="nbpiece" min="1" max="20" required>
			</div>


			<div class="contact__field">
				<label for="selectfield-year" class="selectfield-year">Année de construction ?</label>
				<input list="year">
				<datalist id="year">
					<option value="Avant 1850">
					<option value="1850 - 1913">
					<option value="1914 - 1947">
					<option value="1948 - 1974">
					<option value="1975 - 1984">
					<option value="1985 - 2007">
					<option value="Depuis 2008">
				</datalist>	
			</div>
			
			
			<div class="contact__field">
                <label for="description">Des travaux sont-ils  à prévoir ?</label>
                <div>
				  <input type="radio" id="oui" name="travaux" value="oui" checked>
				  <label for="Maisons">Oui</label>
				</div>
				<div>
				  <input type="radio" id="non" name="travaux" value="non">
				  <label for="non">Non</label>
				</div>
	        </div>

            <!-- Message -->
            <div class="contact__field">
                <label for="description">Décrivez votre bien ou précisez votre demande</label>
                <textarea name="description" id="{{ $.Site.Params.form.inputMsgName }}" form="contactForm"
                    maxlength="{{ $.Site.Params.form.inputMsgLength }}" id="descritpion"
                    arial-labelledby="description" required></textarea>
            </div>

            <!-- Submit -->
            <div class="contact__field">
                <button type="submit" class="ripple-btn submit" onclick="cleanForm" aria-label="Demander une évaluation gratuite">
                    Demander une évaluation gratuite
                </button>
            </div>

        </form>

{{< /rawhtml >}}