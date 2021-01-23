---
title: "Formulaire Demande Estimation"
description: "Formulaire de demande d'estimation gratuite de vote maison ou votre appartement à Luxembourg"
images: []
draft: false
menu: 
weight: 
---

<form action="https://getform.io/f/{YOUR-FORMENDPOINT-GOES-HERE}"  method="POST" accept-charset="UTF-8" class="contact__form"
            id="contactForm">

            <!-- Name -->
            <div class="contact__field contact__field--name">
                <label for="Nom">Nom : </label>
                <input type="text" name="Nom" placeholder="Votre nom"
                    class="contact__form__input contact__form__name" id="nom"
                    aria-labelledby="nom" required>
            </div>

            <!-- Email -->
            <div class="contact__field contact__field--email">
                <label for="Email">Email</label>
                <input type="email" name="Email" placeholder="Email"
                    class="contact__form__input contact__form__email" id="email"
                    aria-labelledby="email" required>
            </div>

            <!-- Message -->
            <div class="contact__field contact__field--msg">
                <label for="description">Décrivez votre bien ou précisez votre demande</label>
                <textarea name="description" id="{{ $.Site.Params.form.inputMsgName }}" form="contactForm"
                    maxlength="{{ $.Site.Params.form.inputMsgLength }}" id="descritpion"
                    arial-labelledby="description" required></textarea>
            </div>

            <!-- Submit -->
            <div class="contact__field contact__field--submit">
                <button type="submit" class="ripple-btn submit" onclick="cleanForm" aria-label="Demander une évaluation gratuite">
                    Demander une évaluation gratuite
                </button>
            </div>

        </form>

