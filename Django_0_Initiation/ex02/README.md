# Exercice 02 - Formulaire de Contact

## 🎯 Objectif
Créer un formulaire HTML qui s'intègre avec le fichier JavaScript `popup.js` fourni.

## 📋 Fichier à créer
`form.html`

## ✅ Champs obligatoires

**Champs texte:**
- `Firstname` - input type="text"
- `Name` - input type="text"

**Champs spécialisés HTML5:**
- `Age` - input type="number"
- `Phone` - input type="tel"
- `Email` - input type="email"

**Autres champs:**
- `Student at 42?` - input type="checkbox"
- `Gender` - input type="radio" (Male, Female, Other)

**Bouton:**
- Submit avec `onclick="displayFormContents();"`

## 🚀 Commandes

```bash
# 1. Lancer ex02
cd Django_0_Initiation
make ex02

# 2. Ouvrir navigateur
# http://localhost:8002/form.html

# 3. Tester: remplir et cliquer Submit
# Une popup s'affiche avec les données ✨

# 4. Arrêter
make clean
```

## 📝 Structure

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Contact Form</title>
  </head>
  <body>
    <h1>Formulaire</h1>
    
    <form>
      <input type="text" name="firstname" />
      <input type="text" name="name" />
      <input type="number" name="age" />
      <input type="tel" name="phone" />
      <input type="email" name="email" />
      <input type="checkbox" name="student" />
      
      <input type="radio" name="gender" value="Male" />
      <input type="radio" name="gender" value="Female" />
      <input type="radio" name="gender" value="Other" />
      
      <button type="button" onclick="displayFormContents();">Submit</button>
    </form>

    <script src="popup.js"></script>
  </body>
</html>
```

## ✨ Résultat

Remplissez le formulaire → Cliquez Submit → Popup avec vos données! 🎉

---

**Prêt?** Lance `make ex02` et commence! 🚀

