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
 "chocolate": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
  ("Pet Poison Helpline: chocolate", "https://www.petpoisonhelpline.com/poison/chocolate/"),
  ("VCA: chocolate poisoning overview", "https://vcahospitals.com/know-your-pet/chocolate-poisoning"),
 ],
 "onions": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
  ("Pet Poison Helpline: onion", "https://www.petpoisonhelpline.com/poison/onion/"),
 ],
 "garlic": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
  ("Pet Poison Helpline: onion (Allium family)", "https://www.petpoisonhelpline.com/poison/onion/"),
 ],
 "chives": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
  ("Pet Poison Helpline: onion (Allium family)", "https://www.petpoisonhelpline.com/poison/onion/"),
 ],
 "grapes": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
  ("Pet Poison Helpline: grapes", "https://www.petpoisonhelpline.com/poison/grapes/"),
 ],
 "raisins": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
  ("Pet Poison Helpline: grapes (includes raisins/currants context)", "https://www.petpoisonhelpline.com/poison/grapes/"),
 ],
 "alcohol": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 ],
 "coffee": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 ],
 "raw-dough": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 ],
 "xylitol": [
  ("ASPCApro: xylitol differences in cats and dogs", "https://www.aspcapro.org/resource/most-common-sleep-aid-toxicities-cats-and-dogs"),
  ("Small cat study (2018)", "https://pubmed.ncbi.nlm.nih.gov/29430681/"),
  ("Pet Poison Helpline: xylitol", "https://www.petpoisonhelpline.com/poison/xylitol/"),
 ],
 "avocado": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
  ("Pet Poison Helpline: avocado", "https://www.petpoisonhelpline.com/poison/avocado/"),
 ],
 "bones": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 ],
 "milk": [
  ("Pet Poison Helpline: milk", "https://www.petpoisonhelpline.com/poison/milk/"),
  ("Cornell Feline Health Center: feeding your cat", "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat"),
 ],
 "cheese": [
  ("Pet Poison Helpline: milk (lactose context)", "https://www.petpoisonhelpline.com/poison/milk/"),
 ],
 "yogurt": [
  ("Pet Poison Helpline: milk (lactose context)", "https://www.petpoisonhelpline.com/poison/milk/"),
 ],
 "tuna": [
  ("Cornell Feline Health Center: feeding your cat", "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat"),
  ("WSAVA Global Nutrition Guidelines", "https://wsava.org/global-guidelines/global-nutrition-guidelines/"),
 ],
 "chicken": [
  ("Cornell Feline Health Center: feeding your cat", "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat"),
  ("WSAVA Global Nutrition Guidelines", "https://wsava.org/global-guidelines/global-nutrition-guidelines/"),
 ],
 "cooked-eggs": [
  ("ASPCA: people foods to avoid (raw eggs / salmonella context)", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 ],
 "raw-eggs": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 ],
 "raw-fish": [
  ("ASPCA: people foods to avoid", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 ],
 "cucumber": [
  ("ASPCA: people foods to avoid (context for unsafe seasonings)", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 ],
 "peanut-butter": [
  ("Pet Poison Helpline: xylitol", "https://www.petpoisonhelpline.com/poison/xylitol/"),
  ("ASPCApro: xylitol differences in cats and dogs", "https://www.aspcapro.org/resource/most-common-sleep-aid-toxicities-cats-and-dogs"),
 ],
}

FOOD_EXTRA = {
 'chocolate': 'Baking chocolate and dark chocolate contain more theobromine per gram than milk chocolate. Wrappers, brownie batter, cocoa powder, mocha drinks and sugar-free chocolate that also contains xylitol all count as exposures. Seasoned or filled chocolates add fat and other ingredients but do not make theobromine safer. Cats are small; even a lick is still worth a professional call rather than a wait-and-see experiment.',
 'onions': 'Onion powder, onion salt, fried onions, soup bases and baby food with onion are easy to miss. Cooking, drying or powdering does not make Allium plants safe for cats. Compared with chives or garlic, the hazard theme is the same—red blood cell damage—while the form on a human plate often looks too small to matter.',
 'garlic': 'Garlic salt, garlic oil, garlic powder and savory broth concentrates are common hidden sources. Garlic is often described as more potent than onion on a weight basis among Allium foods, which is why leftover takeout and seasoned meats are frequent accidental exposures. Treat any intentional sharing of garlic-seasoned food as a vet call, not a home experiment.',
 'chives': 'Chives often appear as a garnish. The concern is the Allium family effect on red blood cells, similar in theme to onion and garlic, even when the portion looks tiny on a human plate.',
 'grapes': 'Because cat-specific toxicity data are limited, CatCalc does not invent a toxic dose for cats. We still advise against offering grapes and prompt veterinary contact after ingestion. Fresh fruit, chopped fruit cups and just-one-grape training treats are the usual household routes; dogs have a clearer kidney-injury record, and that uncertainty is not permission to feed cats.',
 'raisins': 'Raisin bread, trail mix and cereal clusters can combine raisins with chocolate, xylitol or macadamia ingredients. Dried fruit is easy to underestimate by volume. Bring the package to the call if you can. As with grapes, we do not invent a cat-specific toxic dose.',
 'alcohol': 'Uncooked yeast dough, some sauces and spilled drinks are easy ways cats encounter alcohol. Size matters: a small body reaches a dangerous dose quickly.',
 'coffee': "Coffee grounds in compost bins and chewable caffeine tablets are higher-risk than a cold sip of milky coffee, but none of these belong in a cat's reach.",
 'raw-dough': 'Expansion plus alcohol production is the dual hazard. Bread that is fully baked is a different question (see the bread page) and still offers little nutrition.',
 'xylitol': 'Check peanut butter, syrups, gum, mints, dental products and some baked goods. Dog hypoglycemia talking points should not be pasted onto cats without noting the limited feline evidence. Mixed products may also contain chocolate or other hazards—read the full ingredient list for the hotline call.',
 'milk': "Lactose-free cat milk products exist as treats; they are still treats, not a hydration strategy. Growing orphans need commercial kitten milk replacer under proper guidance, never cow's milk as a substitute. Flavored coffee creamers and chocolate milk add caffeine or theobromine risks on top of lactose.",
 'cheese': 'Lactose is lower than in milk, but fat and salt are not free. Soft cheese, hard cheese and cheese sauces differ; sauces often hide onion or garlic. Medication hiding in cheese should be vet-approved for that drug and that cat. A pea-sized nibble is the usual outer bound people discuss—not a cheese board.',
 'yogurt': 'Fruit-on-the-bottom cups, chocolate swirls and sugar-free products with polyols are the usual traps. Plain and unsweetened is the only version worth discussing.',
 'tuna': 'A tuna-only diet can contribute to nutritional imbalance over time. Human canned tuna in brine is salty; oil-packed tuna adds fat. Fish bones in some products are a separate injury risk. Rotate complete cat foods as the staple; keep tuna as a high-value training bit in spring water when you use it at all.',
 'raw-fish': 'Thiaminase in some raw fish and pathogen risk are separate issues from cooked, deboned fish treats. Freezing at home is not a guarantee of safety.',
 'raw-eggs': 'Cooking addresses the main practical risks for household sharing. Seasonings afterward can reintroduce onion or salt problems.',
 'bones': 'Cooked bones are brittle. If a bone is stuck or the cat struggles to breathe, that is emergency care—not an internet search.',
 'dog-food': 'Shared households sometimes leave dog bowls accessible. One stolen kibble is usually not an emergency; months of dog food as the only diet is a nutrition problem.',
 'ham': 'Breakfast meats are very high in salt. If your cat snags a piece, watch for vomiting or diarrhea and choose lean cooked meats next time.',
 'avocado': 'Focus on mechanical risk from the pit and digestive upset from fatty flesh. We state persin evidence limits honestly instead of copying bird or livestock talking points.',
 'peanut-butter': 'Stickiness plus calories plus possible xylitol is a poor combination. A smear on a toy for enrichment is still optional, not required.',
 'bread': 'Plain bread is mostly starch. Garlic bread, seeded breads with toxic mix-ins and raw dough each need their own caution.',
 'banana': 'Cats lack a sweet taste receptor for sugar the way humans do; most shrug at banana. Tiny portions avoid unnecessary sugar load.',
 'apples': 'Core and seeds are the parts to remove. Flesh is the only section we discuss as an optional tiny treat.',
 'chicken': 'Rotisserie seasonings, onion gravy, barbecue sauce and cooked bones undo the benefit of an otherwise suitable lean meat. Plain leftover breast or thigh meat, cooled and shredded, is the template. Raw chicken is a different question (pathogens)—this page is about cooked plain chicken as a small treat.',
 'turkey': 'Holiday leftovers are where garlic, onions, stuffing raisins and bones sneak in. Serve a plain cut piece only.',
 'salmon': 'Fish is still a treat relative to a complete diet. Bones and heavy seasoning are the usual mistakes.',
 'cooked-eggs': "Eggs are nutrient-dense; a whole egg may be too many calories for a small cat's treat budget. Share a bite, not a breakfast plate. Butter, milk, cheese, onion powder or chili oil in scrambled eggs reintroduce problems covered on other pages. Raw eggs are covered separately because of pathogen and avidin concerns.",
 'shrimp': 'Shells and tails are choking hazards. Garlic butter restaurant shrimp is not the same as plain boiled shrimp.',
 'pumpkin': 'Plain puree is not the same as pie filling. Persistent constipation or diarrhea needs a vet, not endless pumpkin experiments.',
 'blueberries': 'Cut berries reduce choking risk for enthusiastic gulpers. Most cats are indifferent; that is fine.',
 'watermelon': 'Rind and seeds are the parts to discard. Flesh is mostly water and sugar—keep cubes small.',
 'strawberries': 'Remove leafy tops. Sugary fruit is optional; complete cat food remains the staple.',
 'cantaloupe': 'Some cats investigate melon aroma. Rind and seeds still go in the compost, not the bowl.',
 'carrots': 'Hard raw chunks are a choking risk. Soft, plain, cut pieces are the only form we describe as a small treat.',
 'cucumber': 'Cucumber is mostly water and novelty for cats that bother to try it. Peel if the skin is waxed; slice thin to reduce gulping. Pickled cucumber brings vinegar and salt; seasoned salads often include onion or garlic. Cucumber is not a hydration plan and not a diet food—complete cat food and fresh water remain the basics.',
 'green-beans': 'A few cats accept them as low-calorie training bits. Butter and garlic turn a caution-free vegetable into a problem.',
 'peas': 'Common in commercial recipes; plain peas as a rare extra are fine for many cats.',
 'rice': 'Sometimes used short-term in bland diets under veterinary direction. It is not a protein substitute.',
 'oatmeal': 'Cook thoroughly with water. Sweeteners, milk and sugar-free syrups do not belong in the pot.',
 'catnip': 'Response is partly genetic. Toys stuffed with catnip should be sized so the cat cannot swallow string or plastic.',
}

# Food-specific detail sections (trusted HTML). Priority foods get deeper original notes.
FOOD_DETAIL = {
 "chocolate": [
  ("Plain vs flavored or filled chocolate",
   "<p>Plain dark or baking chocolate is usually higher in theobromine per gram than milk chocolate. Fillings, nuts, coffee flavoring or liqueur add extra hazards but never cancel methylxanthine risk. “White chocolate” is lower in theobromine than dark chocolate yet still unhelpful fat and sugar for cats—and some sugar-free products add xylitol.</p>"),
  ("What to tell the vet or hotline",
   "<p>Share the product name, cocoa percentage if known, estimated grams eaten, time since exposure, and your cat’s weight. Mention wrappers or batter if those were chewed. Ask the professional whether monitoring at home or clinic care is needed—do not invent a “safe square” of chocolate.</p>"),
  ("Compared with coffee or xylitol sweets",
   "<p>Coffee and tea are caffeine problems; many sugar-free candies are xylitol problems; chocolate can involve theobromine, caffeine, fat and sometimes xylitol together. When the ingredient list is mixed, bring the package rather than guessing which toxin “matters more.”</p>"),
 ],
 "onions": [
  ("Raw, cooked, powdered and leftover sauces",
   "<p>All common culinary forms matter: raw slices, caramelized onions, onion powder in seasoning blends, and onion in broth or baby food. Heat does not remove the Allium hazard for cats.</p>"),
  ("What to tell the vet",
   "<p>Estimate how much onion-containing food was eaten, whether it was powder or fresh, and when. Mention pale gums, weakness, lethargy or dark urine if present—signs can lag. There is no home antidote dose to calculate from a blog.</p>"),
  ("Compared with garlic and chives",
   "<p>Garlic and chives are the same Allium family concern. Powdered garlic in leftovers is a frequent hidden source; chives as garnish look tiny on a human plate and still count.</p>"),
 ],
 "garlic": [
  ("Hidden garlic in human food",
   "<p>Garlic powder, garlic salt, garlic oil, and “savory” broths show up in rotisserie seasoning, noodle cups and leftovers. A cat that licks a garlic-butter plate is an exposure even if no clove was offered on purpose.</p>"),
  ("What to tell the vet",
   "<p>Describe the dish, rough amount, time, and any vomiting or lethargy. Bring labels when garlic is one of many ingredients. Do not wait days “to see” if the portion seemed small.</p>"),
  ("Compared with onions",
   "<p>Both are Allium plants linked to red blood cell injury in cats. Onion pages and garlic pages exist separately so searchers find either name; the action after ingestion is the same: professional advice, not a homemade dose chart.</p>"),
 ],
 "grapes": [
  ("Fresh fruit vs fruit cups and desserts",
   "<p>Whole grapes, chopped fruit cups, and desserts that include grapes all count. Raisins are covered on their own page because dried fruit is easy to underestimate and often mixed with other ingredients.</p>"),
  ("Evidence limits (read before sharing dog advice)",
   "<p>Kidney injury from grapes and raisins is better documented in dogs. Cat-specific toxic dose data are limited. CatCalc therefore says <em>avoid</em> and <em>call a vet after ingestion</em>—we do not invent a feline “safe number of grapes.”</p>"),
  ("What to tell the vet",
   "<p>How many grapes (or how much chopped fruit), approximate time, whether seeds/skin were included, and your cat’s weight. Early calls beat waiting for vomiting or lethargy.</p>"),
 ],
 "raisins": [
  ("Where raisins hide",
   "<p>Trail mix, oatmeal cookies, cinnamon rolls, and cereal clusters are common sources. Other ingredients (chocolate, xylitol, nuts) may matter as much as the raisin count.</p>"),
  ("What to tell the vet",
   "<p>Bring the package. Estimate pieces eaten and time. Say clearly if sugar-free sweeteners appear on the label. As with grapes, we do not provide a cat-specific toxic dose table.</p>"),
 ],
 "xylitol": [
  ("Where xylitol appears",
   "<p>Sugar-free gum, mints, some peanut butters, syrups, dental products and baked goods may list xylitol or “birch sugar.” If the label is unclear, treat unknown sugar-free products as a hotline question.</p>"),
  ("Cats are not small dogs",
   "<p>A small study in healthy cats did not reproduce the classic low-blood-sugar pattern famous in dogs; gastrointestinal upset is still described in feline poison-control summaries. Limited evidence is not a safety claim for every dose, product mix, or sick cat.</p>"),
  ("What to tell the vet",
   "<p>Read the full ingredient list aloud, estimate amount chewed or swallowed, and note chocolate or other co-ingestants. Ask whether observation or clinic care is advised—do not induce vomiting on internet advice alone.</p>"),
 ],
 "milk": [
  ("Cow’s milk vs kitten milk replacer",
   "<p>Most adult cats digest lactose poorly after weaning, so ordinary cow’s milk often causes soft stool or diarrhea. Orphaned kittens need commercial kitten milk replacer and veterinary feeding guidance—not dairy from the fridge.</p>"),
  ("Lactose-free “cat milk” and flavored drinks",
   "<p>Lactose-free cat milk products are still optional treats. Chocolate milk, coffee drinks and creamers can add caffeine or theobromine hazards on top of dairy fat.</p>"),
  ("What to tell the vet after a large drink",
   "<p>Share volume, milk type, and whether diarrhea or vomiting started. Persistent diarrhea, kitten dehydration, or mixed toxic ingredients deserve a call—not another bowl of milk.</p>"),
 ],
 "cheese": [
  ("Plain cheese vs sauces",
   "<p>A pea-sized bit of plain cheese is what people usually mean by “a nibble.” Cheese sauces, nacho cheese and seasoned soft cheeses often include onion, garlic or heavy salt.</p>"),
  ("Fat, salt and medication tricks",
   "<p>Lower lactose than milk does not make cheese a free food. High fat can upset some cats. Hiding pills in cheese is only appropriate when your vet agrees for that drug and that patient.</p>"),
  ("Compared with milk and yogurt",
   "<p>Milk is usually worse for lactose; yogurt must be plain and unsweetened if used at all; cheese concentrates fat and salt. None of these replace a complete cat diet.</p>"),
 ],
 "tuna": [
  ("Spring water vs brine or oil",
   "<p>Prefer plain tuna in spring water as an occasional high-value bit. Brine adds salt; oil adds fat. Seasoned pouches with broth may hide onion or garlic powder—read labels.</p>"),
  ("Treat vs staple diet",
   "<p>Cats may prefer tuna to balanced cat food. Making tuna the main diet risks nutritional gaps over time. Complete commercial cat food (or a vet-designed home-prepared diet) should remain the staple.</p>"),
  ("What to tell the vet",
   "<p>If a tuna binge led to vomiting, diarrhea or refusal of normal food, say how much tuna, which packing liquid, and how long tuna has been a large share of calories.</p>"),
 ],
 "chicken": [
  ("Safe parts and preparations",
   "<p>Plain cooked, boneless, skinless meat is the usual small-treat template. Remove cooked bones (splinter risk). Skip fried coatings, salt, garlic, onion and gravy.</p>"),
  ("Raw vs cooked",
   "<p>This page is about cooked chicken. Raw poultry can carry pathogens; raw feeding decisions belong with your veterinarian, not a leftover-sharing tip sheet.</p>"),
  ("Compared with turkey or ham",
   "<p>Plain cooked turkey follows similar rules. Ham and bacon are caution foods because of salt and fat. Holiday platters are where bones and seasoned skins sneak in.</p>"),
 ],
 "cooked-eggs": [
  ("Fully cooked, unseasoned only",
   "<p>Hard-boiled or plain scrambled egg without butter, milk, cheese, salt chili oil or onion powder can be a small treat. Restaurant omelets are not the same food.</p>"),
  ("Portion and calories",
   "<p>Eggs are calorie-dense. A bite or two is the usual outer bound for a treat budget; a whole egg may crowd out balanced cat food calories for a small cat.</p>"),
  ("Compared with raw eggs",
   "<p>Raw eggs bring pathogen risk and avidin in raw whites that can interfere with biotin absorption when fed routinely. Prefer fully cooked eggs if you share egg at all.</p>"),
 ],
 "cucumber": [
  ("Plain flesh vs pickles and salads",
   "<p>Peeled, thinly sliced plain cucumber flesh is the only form we describe as a small optional treat. Pickles add salt and vinegar; mixed salads often include onion, garlic or dressing.</p>"),
  ("How it compares with other produce",
   "<p>Like many watery vegetables, cucumber is novelty more than nutrition for obligate carnivores. Blueberries or pumpkin have their own pages and still must stay inside treat calories.</p>"),
  ("When to skip it",
   "<p>Skip cucumber if your cat has ongoing digestive disease unless your vet says otherwise, and skip any preparation you would not describe as plain and unsalted.</p>"),
 ],
}

