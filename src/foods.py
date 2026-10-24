# Recommendation groups; individual labels and conclusions below are authoritative.
FOODS = [
 # ---- NO ----
 ("chocolate","Chocolate","no","Chocolate contains theobromine and caffeine, which cats cannot break down well. Even small amounts can cause vomiting, diarrhea, a racing heart, tremors and seizures. Dark and baking chocolate are the most dangerous.","Call your vet or a pet poison hotline right away, even if your cat seems fine. Note the type and amount eaten."),
 ("onions","Onions","no","Onions (raw, cooked, powdered or in sauces) belong to the Allium family. They damage cats' red blood cells and can cause anemia. Cats are more sensitive to Allium plants than dogs.","Contact your vet. Signs such as weakness, pale gums or red-brown urine can appear days later."),
 ("garlic","Garlic","no","Garlic is an Allium like onions and is considered even more potent. Garlic powder in broths, baby food and leftovers is a common hidden source.","Contact your vet, and check labels of any human food or broth you share with your cat."),
 ("chives","Chives","no","Chives, leeks and scallions are Allium plants and can damage red blood cells in cats.","Contact your vet if your cat ate a noticeable amount."),
 ("grapes","Grapes","no","Grapes can cause kidney injury in dogs. Cat-specific evidence is limited; the canine mechanism and toxic dose should not be assumed to apply to cats. This uncertainty is not a reason to offer grapes.","Avoid feeding grapes. If eaten, contact your vet promptly with the amount and time; do not wait for symptoms."),
 ("raisins","Raisins","no","Raisins are dried grapes. Kidney toxicity is established in dogs, but cat-specific evidence is limited. Raisin bread, trail mix and cereal may contain other harmful ingredients too.","Do not offer raisins. Contact your vet promptly after ingestion with the product and amount."),
 ("alcohol","Alcohol","no","Alcohol is absorbed quickly and a cat's small body is affected by tiny amounts, causing vomiting, disorientation, breathing problems and potentially death.","Treat as an emergency and call your vet."),
 ("coffee","Coffee","no","Coffee, tea and energy drinks contain caffeine, which can cause restlessness, rapid breathing, heart palpitations and tremors in cats.","Call your vet if your cat drank or licked coffee grounds, beans or caffeine pills."),
 ("raw-dough","Raw Bread Dough","no","Raw yeast dough can expand in the stomach and the fermenting yeast produces alcohol. Both are dangerous for cats.","Treat as an emergency and call your vet."),
 ("xylitol","Xylitol (Sugar-Free Gum & Sweets)","no","Dog toxicity should not be applied to cats. A small study of six healthy cats did not find the low blood sugar or liver effects seen in dogs; ASPCApro describes gastrointestinal upset in cats. The limited study does not establish safety for all cats, doses or mixed products.","Do not feed xylitol products. After ingestion, contact your vet or a poison hotline with the ingredient list; other ingredients may be hazardous."),
 # ---- CAUTION ----
 ("milk","Milk","caution","Most adult cats become lactose intolerant after weaning, so cow's milk often causes upset stomach and diarrhea. Kittens should get kitten milk replacer, never cow's milk.","If you want to offer milk, use a lactose-free 'cat milk' as an occasional treat."),
 ("cheese","Cheese","caution","Cheese has less lactose than milk, but it is high in fat and salt. A tiny nibble may be tolerated; larger amounts may cause tummy trouble.","If tolerated, keep it as a rare, tiny treat. Ask your vet before using food to give medication."),
 ("yogurt","Yogurt","caution","Plain, unsweetened yogurt is lower in lactose than milk and some cats tolerate a small spoonful. Avoid flavored yogurts and any containing xylitol or chocolate.","Start with a teaspoon and watch for diarrhea."),
 ("tuna","Tuna","caution","Cats love tuna, but human canned tuna is not a complete diet and a tuna-heavy diet has been linked to nutritional problems. Tuna packed in brine is also salty.","Offer tuna in spring water only as an occasional treat, not a meal replacement."),
 ("raw-fish","Raw Fish","caution","Some raw fish contain thiaminase, an enzyme that destroys vitamin B1 (thiamine), and raw fish can carry bacteria and parasites.","Cook fish plainly and remove bones before sharing."),
 ("raw-eggs","Raw Eggs","caution","Raw eggs can carry Salmonella or E. coli, and raw egg white contains avidin, which can interfere with biotin absorption.","Cook eggs fully (scrambled or boiled, no seasoning)."),
 ("bones","Cooked Bones","no","Cooked bones become brittle and can splinter, causing choking or injuries to the mouth and gut. Raw bones also carry injury and infection risks.","Do not give cooked bones. If swallowed, contact your vet promptly; choking or breathing difficulty requires emergency care."),
 ("dog-food","Dog Food","caution","A bite of dog food will not hurt, but dog food does not meet cats' needs. Cats require more protein and nutrients such as taurine and arachidonic acid.","Never use dog food as your cat's regular diet."),
 ("ham","Ham & Bacon","caution","Processed meats are very high in salt and fat, which can upset the stomach and, over time, contribute to pancreatitis and obesity.","A tiny bite is unlikely to harm, but better treats exist."),
 ("avocado","Avocado","no","Severe persin toxicity is best documented in other species; cat-specific evidence is limited. The pit can cause choking or obstruction, and the fatty flesh may cause digestive upset.","Avoid feeding it on purpose. Contact your vet after pit ingestion, a large amount, or any symptoms."),
 ("peanut-butter","Peanut Butter","caution","Peanut butter is not toxic, but it is sticky, high in fat and calories, and some brands contain xylitol.","Check the label for xylitol and offer no more than a lick."),
 ("bread","Bread","caution","Plain baked bread is not toxic, but it offers cats almost no nutrition. Garlic bread, raisin bread and raw dough are dangerous.","A small piece of plain bread is fine occasionally."),
 ("banana","Banana","caution","Banana is not toxic but is high in sugar, and cats cannot taste sweetness. A small slice will not hurt most cats.","Offer a thumbnail-sized piece at most."),
 ("apples","Apples","caution","Apple flesh is fine in small amounts, but the ASPCA notes that stems, leaves and seeds contain cyanogenic compounds.","Offer a small piece of peeled flesh with the core and seeds removed."),
 # ---- YES ----
 ("chicken","Cooked Chicken","yes","Plain cooked chicken is lean protein that cats naturally thrive on. It is one of the best human foods to share.","Serve boneless, skinless and unseasoned (no garlic, onion or salt)."),
 ("turkey","Cooked Turkey","yes","Plain cooked turkey breast is a safe, high-protein treat.","Skip the skin, gravy, stuffing and bones."),
 ("salmon","Cooked Salmon","yes","Cooked salmon provides protein and omega-3 fatty acids.","Cook plainly, remove all bones and keep portions small."),
 ("cooked-eggs","Cooked Eggs","yes","Fully cooked eggs are a good source of protein and amino acids for cats.","Scramble or boil with no butter, salt or seasoning."),
 ("shrimp","Cooked Shrimp","yes","Plain cooked shrimp is a tasty, high-protein treat most cats love.","Remove the shell, tail and digestive tract; no garlic butter."),
 ("pumpkin","Pumpkin","yes","Plain cooked or canned pumpkin contains fiber; it is not a treatment for an unexplained digestive problem. Pie filling may contain sugar, spices or other unsuitable ingredients.","Offer only a small amount of plain pumpkin. Ask your vet about ongoing constipation or diarrhea."),
 ("blueberries","Blueberries","yes","Blueberries are non-toxic and full of antioxidants. Many cats ignore them, but they are a safe low-calorie treat.","Offer one or two, cut in half for small cats."),
 ("watermelon","Watermelon","yes","Seedless watermelon flesh is safe and hydrating.","Remove all seeds and rind; offer a small cube."),
 ("strawberries","Strawberries","yes","Strawberries are non-toxic for cats, though sugary.","Offer a small piece with the leaves removed."),
 ("cantaloupe","Cantaloupe","yes","Many cats are attracted to cantaloupe's smell. The flesh is safe in small amounts.","Remove the rind and seeds."),
 ("carrots","Carrots","yes","Cooked carrots are safe. Raw carrot pieces can be a choking hazard.","Steam or boil and cut into small pieces."),
 ("cucumber","Cucumber","yes","Cucumber is mostly water and safe for cats in small amounts.","Peel and slice thinly."),
 ("green-beans","Green Beans","yes","Plain cooked green beans are low in calories and safe for cats.","No salt, butter or garlic."),
 ("peas","Peas","yes","Peas are common in commercial cat food and safe plain.","Cooked or thawed frozen peas, no seasoning."),
 ("rice","Rice","yes","Plain cooked white rice is easy to digest and sometimes recommended for short bland diets.","Plain and cooked only; it should not replace meat."),
 ("oatmeal","Oatmeal","yes","Plain cooked oats are safe and contain fiber.","Cook with water (not milk) and serve a small amount."),
 ("catnip","Catnip","yes","Catnip is non-toxic. About half to two-thirds of cats respond to it with playful behavior.","If a cat eats a lot, it may vomit or have diarrhea; offer in moderation."),
]

# Each tuple: visible label, short conclusion, handling heading, related-food category.
# No group-wide claim of toxicity or permission to feed overrides these conclusions.
FOOD_GUIDANCE = {
 "chocolate": ("Do not feed", "Chocolate contains toxic methylxanthines; contact your vet after ingestion.", "What to do", "hazards"),
 "onions": ("Do not feed", "Onions can damage cats' red blood cells, including cooked or powdered onion.", "What to do", "hazards"),
 "garlic": ("Do not feed", "Garlic can damage red blood cells; avoid it in all forms.", "What to do", "hazards"),
 "chives": ("Do not feed", "Chives and other Alliums can damage cats' red blood cells.", "What to do", "hazards"),
 "grapes": ("Avoid · limited evidence", "Avoid grapes: cat-specific toxicity evidence is limited; consult your vet after ingestion.", "What to do", "hazards"),
 "raisins": ("Avoid · limited evidence", "Avoid raisins: cat-specific toxicity evidence is limited; consult your vet after ingestion.", "What to do", "hazards"),
 "alcohol": ("Do not feed", "Alcohol can cause serious poisoning; ingestion requires urgent veterinary advice.", "What to do", "hazards"),
 "coffee": ("Do not feed", "Caffeine can poison cats; keep coffee, grounds and beans away.", "What to do", "hazards"),
 "raw-dough": ("Do not feed", "Raw yeast dough can expand and produce alcohol in the stomach.", "What to do", "hazards"),
 "xylitol": ("Avoid · limited evidence", "Do not feed xylitol products. Cat evidence is limited; do not assume dog toxicity applies.", "What to do", "hazards"),
 "milk": ("Caution · lactose", "Cow's milk often causes digestive upset; it is not a kitten milk replacement.", "Milk alternatives", "pantry"),
 "cheese": ("Caution · fat and salt", "Only a rare tiny piece if tolerated; cheese may cause digestive upset.", "If offering cheese", "pantry"),
 "yogurt": ("Caution · plain only", "A small amount of plain unsweetened yogurt may be tolerated; check ingredients.", "If offering yogurt", "pantry"),
 "tuna": ("Caution · treat only", "Plain tuna in spring water is an occasional treat, never a complete diet.", "How to serve it", "protein"),
 "raw-fish": ("Cook first", "Do not serve raw fish. Cook it plainly and remove bones before sharing.", "Cook before serving", "protein"),
 "raw-eggs": ("Cook first", "Do not serve raw eggs. Cook eggs fully without seasoning before sharing.", "Cook before serving", "protein"),
 "bones": ("Do not feed", "Do not feed cooked bones: they can splinter, choke or injure a cat.", "What to do", "hazards"),
 "dog-food": ("Not a cat diet", "An accidental bite is usually not harmful, but dog food cannot replace a complete cat diet.", "Choose a complete cat diet", "protein"),
 "ham": ("Caution · salt and fat", "Avoid routine feeding of ham or bacon; a tiny bite is unlikely to harm most healthy cats.", "Choose a plainer treat", "protein"),
 "avocado": ("Avoid · pit and fat", "Avoid feeding avocado; the pit and fat pose risks, and cat-specific persin evidence is limited.", "What to do", "produce"),
 "peanut-butter": ("Caution · ingredients", "At most a lick of xylitol-free peanut butter; it is sticky and high in fat.", "Check ingredients first", "pantry"),
 "bread": ("Caution · plain baked only", "Only a small piece of plain baked bread; avoid raw dough, garlic and raisin breads.", "How to serve it", "pantry"),
 "banana": ("Caution · tiny portion", "A very small peeled banana piece can be an occasional treat, not a meal.", "How to serve it", "produce"),
 "apples": ("Caution · flesh only", "Only a small piece of apple flesh with the core, seeds and stems removed.", "How to serve it", "produce"),
 "chicken": ("Small treat · cooked", "Plain cooked chicken can be a small treat; remove skin and bones.", "How to serve it", "protein"),
 "turkey": ("Small treat · cooked", "Plain cooked turkey can be a small treat without skin, gravy, stuffing or bones.", "How to serve it", "protein"),
 "salmon": ("Small treat · cooked", "Offer only a small amount of plain cooked salmon with all bones removed.", "How to serve it", "protein"),
 "cooked-eggs": ("Small treat · fully cooked", "Fully cooked egg can be a small treat without butter, salt or seasoning.", "How to serve it", "protein"),
 "shrimp": ("Small treat · cooked", "Plain cooked shrimp can be a small treat with the shell and tail removed.", "How to serve it", "protein"),
 "pumpkin": ("Small treat · plain", "Offer a small amount of plain pumpkin, not sweetened or spiced pie filling.", "How to serve it", "produce"),
 "blueberries": ("Small treat", "Offer only one or two blueberries, cut in half for small cats.", "How to serve it", "produce"),
 "watermelon": ("Small treat · flesh only", "Offer a small watermelon cube with all seeds and rind removed.", "How to serve it", "produce"),
 "strawberries": ("Small treat", "Offer only a small strawberry piece with the leaves removed.", "How to serve it", "produce"),
 "cantaloupe": ("Small treat · flesh only", "Offer a small cantaloupe piece with rind and seeds removed.", "How to serve it", "produce"),
 "carrots": ("Small treat · cooked", "Offer soft cooked carrot cut into small pieces; raw chunks can cause choking.", "How to serve it", "produce"),
 "cucumber": ("Small treat", "Offer a small amount of peeled cucumber sliced thinly.", "How to serve it", "produce"),
 "green-beans": ("Small treat · cooked", "Offer a little plain cooked green bean without salt, butter or garlic.", "How to serve it", "produce"),
 "peas": ("Small treat · plain", "Offer a small amount of plain cooked or thawed peas without seasoning.", "How to serve it", "produce"),
 "rice": ("Small treat · cooked", "Only a little plain cooked rice; it cannot replace a complete cat diet.", "How to serve it", "pantry"),
 "oatmeal": ("Small treat · water-cooked", "Offer a little plain oatmeal cooked with water, not milk or sweeteners.", "How to serve it", "pantry"),
 "catnip": ("Moderation", "Offer a small amount of catnip; eating too much can cause vomiting or diarrhea.", "How to offer it", "produce"),
}

RELATED_PAIRS = [
 ("raw-eggs", "cooked-eggs"), ("raw-fish", "salmon"), ("raw-fish", "tuna"),
 ("grapes", "raisins"), ("onions", "garlic"), ("onions", "chives"),
 ("garlic", "chives"), ("milk", "cheese"), ("milk", "yogurt"),
 ("bread", "raw-dough"), ("chicken", "bones"), ("turkey", "bones"),
 ("peanut-butter", "xylitol"),
]

def related_foods(slug):
    """Stable explicit associations, then a balanced ring within food categories."""
    by_slug = {f[0]: f for f in FOODS}
    peers = sorted(s for s in by_slug if FOOD_GUIDANCE[s][3] == FOOD_GUIDANCE[slug][3])
    index = peers.index(slug)
    selected = [b if a == slug else a for a, b in RELATED_PAIRS if slug in (a, b)]
    # Every page receives links from at least three different category peers.
    selected += [peers[(index + step) % len(peers)] for step in (1, 2, 3)]
    return [by_slug[s] for s in dict.fromkeys(selected) if s != slug]

FOOD_SOURCES = {
 "xylitol": [("ASPCApro: xylitol differences in cats and dogs", "https://www.aspcapro.org/resource/most-common-sleep-aid-toxicities-cats-and-dogs"), ("Small cat study (2018)", "https://pubmed.ncbi.nlm.nih.gov/29430681/")],
}
