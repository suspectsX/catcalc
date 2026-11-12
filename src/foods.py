# Recommendation groups; individual labels and conclusions below are authoritative.
FOODS = [('chocolate',
  'Chocolate',
  'no',
  'Chocolate contains the methylxanthines theobromine and caffeine, which can affect the heart and nervous system. '
  'Cocoa powder and baking chocolate are generally more concentrated than milk chocolate. The product and amount '
  'matter when a veterinarian assesses an exposure.',
  'Call your vet or a pet poison hotline right away, even if your cat seems fine. Note the type and amount eaten.'),
 ('onions',
  'Onions',
  'no',
  "Onions can cause oxidative injury to cats' red blood cells and hemolytic anemia. Raw, cooked, dehydrated and "
  'powdered onions remain a concern; signs of anemia can be delayed after ingestion.',
  'Contact your vet. Signs such as weakness, pale gums or red-brown urine can appear days later.'),
 ('garlic',
  'Garlic',
  'no',
  "Garlic is an Allium plant that can damage cats' red blood cells and cause hemolytic anemia. Fresh cloves, cooked "
  'garlic and concentrated forms require attention after ingestion.',
  'Contact your vet, and check labels of any human food or broth you share with your cat.'),
 ('chives',
  'Chives',
  'no',
  "Chives are Allium plants that can damage cats' red blood cells. Their use as a small garnish does not make "
  'intentional feeding appropriate.',
  'Do not offer chives or chive-seasoned foods. If your cat ate them, contact your veterinarian with the amount, '
  'timing and complete dish or plant description.'),
 ('grapes',
  'Grapes',
  'no',
  'Grape-related acute kidney injury is established in dogs. Published feline evidence remains limited, so CatCalc '
  'advises against offering grapes and recommends veterinary advice after ingestion without assuming that dogs and '
  'cats share a toxic dose.',
  'Avoid feeding grapes. If eaten, contact your vet promptly with the amount and time; do not wait for symptoms.'),
 ('raisins',
  'Raisins',
  'no',
  'Raisins are dried grapes. Kidney injury is well documented in dogs, while feline research remains limited. Do not '
  'offer raisins; seek veterinary advice after a cat eats them, and identify other ingredients in the product.',
  'Do not offer raisins. Contact your vet promptly after ingestion with the product and amount.'),
 ('alcohol',
  'Alcohol',
  'no',
  'Alcohol can cause serious poisoning in cats. Ethanol can depress the nervous system and disrupt normal body '
  'function; a suspected ingestion warrants prompt veterinary advice.',
  'Treat as an emergency and call your vet.'),
 ('coffee',
  'Coffee',
  'no',
  'Caffeine can poison cats. Coffee drinks, beans, grounds and caffeine-containing supplements differ substantially, '
  'so veterinary assessment should use the actual product and estimated amount.',
  'Call your vet if your cat drank or licked coffee grounds, beans or caffeine pills.'),
 ('raw-dough',
  'Raw Bread Dough',
  'no',
  'Raw yeast-based dough can expand in the stomach and produce ethanol as yeast ferments. These mechanical and '
  'alcohol-related hazards require prompt veterinary advice after ingestion.',
  'Treat as an emergency and call your vet.'),
 ('xylitol',
  'Xylitol (Sugar-Free Gum & Sweets)',
  'no',
  'Do not intentionally feed xylitol products. The severe low-blood-sugar and liver effects known in dogs were not '
  'found in a small study of healthy cats; that limited evidence does not clear every mixed product or circumstance.',
  'Do not feed xylitol products. After ingestion, contact your vet or a poison hotline with the ingredient list; '
  'other ingredients may be hazardous.'),
 ('milk',
  'Milk',
  'caution',
  "Many cats digest lactose poorly, and cow's milk can cause diarrhea or other digestive upset. Milk is not a "
  'necessary addition to a complete feline diet.',
  'Avoid routine milk feeding. For an unweaned or orphaned kitten, ask a veterinarian for an appropriate '
  'milk-replacer and feeding plan.'),
 ('cheese',
  'Cheese',
  'caution',
  'Cheese is an optional dairy food that some cats tolerate poorly. Ingredients, calories, salt and lactose vary by '
  'product, so it is not a necessary or routine feline treat.',
  'Avoid routine cheese rewards. Ask the prescribing clinic before hiding medication in cheese or another food.'),
 ('yogurt',
  'Yogurt',
  'caution',
  'Yogurt is an optional dairy food, and lactose or other ingredients may cause digestive upset. A live-culture '
  'claim does not establish a treatment benefit for cats.',
  'Do not use yogurt to treat diarrhea. Ask your veterinarian before adding it, especially for a cat on a prescribed '
  'diet.'),
 ('tuna',
  'Tuna',
  'caution',
  'Human canned tuna is not a complete cat diet. Plain tuna may be an occasional reward if appropriate for the cat, '
  'but the packing liquid, seasoning and overall diet matter.',
  'If your veterinarian allows it, reserve plain tuna for a small occasional reward and continue a complete feline '
  'diet.'),
 ('raw-fish',
  'Raw Fish',
  'caution',
  'Some raw fish contain thiaminases that can deplete vitamin B1 when fed repeatedly, and raw animal foods can '
  'transmit pathogens. Cooking does not make a fish-only diet nutritionally complete.',
  'Do not offer raw fish. If sharing fish, cook it plainly, inspect for bones and keep it an occasional extra within '
  "the cat's feeding plan."),
 ('raw-eggs',
  'Raw Eggs',
  'caution',
  'Raw eggs can carry harmful bacteria. Avidin in raw egg white binds biotin and can interfere with its absorption, '
  'particularly with repeated feeding in an unbalanced diet.',
  'Avoid raw eggs. Any occasional egg reward should be fully cooked and plain, without milk, butter or seasoning.'),
 ('bones',
  'Cooked Bones',
  'no',
  'Cooked bones can lodge in the mouth, throat or digestive tract and cause injury. Raw bones also pose injury and '
  'pathogen risks. Do not offer bones as a cat treat, and seek veterinary advice after one is swallowed.',
  'Do not give cooked bones. If swallowed, contact your vet promptly; choking or breathing difficulty requires '
  'emergency care.'),
 ('dog-food',
  'Dog Food',
  'caution',
  'An accidental bite of ordinary dog food is usually not an emergency, but dog diets do not meet feline nutritional '
  'requirements and should not replace complete cat food.',
  "Feed a complete diet labeled for the cat's species and life stage. Contact your veterinarian if dog food has "
  'supplied regular meals or the food contained medication.'),
 ('ham',
  'Ham & Bacon',
  'caution',
  'Ham and bacon are variable processed meats that may add considerable salt, calories or unsuitable seasonings. '
  'They are poor routine rewards; a tiny plain accidental bite is not automatically poisoning.',
  'Choose a clinic-approved plain reward instead. After a large, heavily seasoned or symptomatic exposure, contact '
  'your veterinarian with the product details.'),
 ('avocado',
  'Avocado',
  'no',
  'Avocado risks differ across species, and severe persin effects in birds or farm animals should not be assumed to '
  'describe cats. Avoid intentional feeding; the pit can obstruct the digestive tract, and mixed dishes may contain '
  'other hazardous ingredients.',
  'Avoid feeding it on purpose. Contact your vet after pit ingestion, a large amount, or any symptoms.'),
 ('peanut-butter',
  'Peanut Butter',
  'caution',
  'Peanut butter is an unnecessary, energy-dense, sticky extra. Ingredients vary, and feline xylitol evidence should '
  'be distinguished from established dog toxicity.',
  'Prefer an easily measured feline reward. If peanut butter was eaten, check the whole ingredient list and contact '
  'your veterinarian for a concerning amount, ingredient or symptom.'),
 ('bread',
  'Bread',
  'caution',
  'A small occasional piece of plain, fully baked bread is different from raw yeast dough or bread containing '
  'hazardous ingredients. Bread is an optional extra, not a substitute for complete cat food.',
  'A small piece of plain bread is fine occasionally.'),
 ('banana',
  'Banana',
  'caution',
  'Peeled banana flesh can be an optional small treat for some healthy cats. It is not a balanced food or a '
  'treatment for a suspected nutrient deficiency.',
  'Offer a thumbnail-sized piece at most.'),
 ('apples',
  'Apples',
  'caution',
  'Plain apple flesh can be an optional small treat. The core, seeds, stems and leaves should be removed; ASPCA '
  'identifies cyanogenic compounds in these plant parts.',
  'Offer a small piece of peeled flesh with the core and seeds removed.'),
 ('chicken',
  'Cooked Chicken',
  'yes',
  'Plain cooked chicken can be an occasional protein-containing reward, but muscle meat alone is not a complete '
  'feline diet and may not suit every medical feeding plan.',
  "Serve only a small amount of fully cooked, boneless, skinless, unseasoned chicken if it fits the cat's diet."),
 ('turkey',
  'Cooked Turkey',
  'yes',
  'Plain fully cooked turkey can be a small occasional reward. Brine, seasonings, gravy, stuffing and bones require '
  'separate checks, and turkey meat alone is not a complete cat diet.',
  'Set aside boneless, skinless, unseasoned turkey before adding human sauces; serve only a small cooled portion if '
  "the cat's feeding plan allows it."),
 ('salmon',
  'Cooked Salmon',
  'yes',
  'Plain cooked salmon can be an occasional fish reward. A kitchen serving is not an omega-3 treatment or a complete '
  'feline diet, and bones and seasonings need separate checks.',
  "Cook a plain portion thoroughly, inspect it for bones, cool and flake it, and keep it within the cat's approved "
  'treat allowance.'),
 ('cooked-eggs',
  'Cooked Eggs',
  'yes',
  'Fully cooked plain egg can be an occasional food reward, but it is not a required supplement or a complete feline '
  'diet. Preparation and total treat calories matter.',
  "Cook until white and yolk are firm, cool, and offer only a small plain portion if it fits the cat's feeding "
  'plan.'),
 ('shrimp',
  'Cooked Shrimp',
  'yes',
  'Plain cooked shrimp can be an occasional reward if suitable for the cat. Shells, tails, seasoning and the overall '
  'diet need separate checks; shrimp is not a complete meal.',
  'Serve only a small cooled piece of fully cooked, unseasoned shrimp with head, shell and tail removed.'),
 ('pumpkin',
  'Pumpkin',
  'yes',
  'Plain pumpkin contains fiber, but it is not a universal treatment for constipation or diarrhea. Straining with '
  'little or no urine is an emergency, not a reason to wait for pumpkin to work.',
  'Use only plain prepared pumpkin if appropriate for your cat. Ask your veterinarian about persistent stool changes '
  'and any symptom-directed amount.'),
 ('blueberries',
  'Blueberries',
  'yes',
  'Plain blueberries can be an occasional treat for some cats. A berry snack has no established role here as a '
  'treatment or disease-prevention supplement.',
  'Offer one or two, cut in half for small cats.'),
 ('watermelon',
  'Watermelon',
  'yes',
  'A little plain seedless watermelon flesh can be an optional treat. It does not replace drinking water or '
  'veterinary assessment of suspected dehydration.',
  'Remove all seeds and rind; offer a small cube.'),
 ('strawberries',
  'Strawberries',
  'yes',
  'Plain strawberry flesh can be an optional small treat for some cats. Strawberry desserts must be assessed by all '
  'their ingredients, and the fruit is not a needed vitamin-C supplement.',
  'Offer a small piece with the leaves removed.'),
 ('cantaloupe',
  'Cantaloupe',
  'yes',
  'A small amount of plain cantaloupe flesh can be an optional treat. It is not a balanced meal, and a larger '
  'serving may cause digestive upset.',
  'Remove the rind and seeds.'),
 ('carrots',
  'Carrots',
  'yes',
  'A little soft plain cooked carrot can be an occasional snack. Cats cannot use its beta-carotene as a substitute '
  'for required preformed vitamin A; hard chunks also need care.',
  'Steam or boil and cut into small pieces.'),
 ('cucumber',
  'Cucumber',
  'yes',
  'A little plain garden cucumber can be an optional snack. Pickles and dressed cucumber dishes require a separate '
  'ingredient assessment; cucumber does not treat dehydration or constipation.',
  'Peel and slice thinly.'),
 ('green-beans',
  'Green Beans',
  'yes',
  'A little plain tender green bean can be an optional snack. Replacing a large share of complete cat food with '
  'beans is not a balanced weight-management plan.',
  'No salt, butter or garlic.'),
 ('peas',
  'Peas',
  'yes',
  'A little plain cooked or thawed garden pea can be an optional extra. A pea ingredient in formulated cat food does '
  'not mean household peas are needed or can replace complete nutrition.',
  'Cooked or thawed frozen peas, no seasoning.'),
 ('rice',
  'Rice',
  'yes',
  'Cats can use properly cooked rice, but rice is not complete nutrition or a universal diarrhea treatment. A '
  'veterinarian should choose the diet for an unwell cat.',
  'Offer only a little plain well-cooked rice if appropriate. For a symptom-directed diet, use the exact food and '
  'amount recommended by your veterinarian.'),
 ('oatmeal',
  'Oatmeal',
  'yes',
  'A little plain oatmeal cooked with water may be an optional extra. It is not a complete cat meal or a treatment '
  'for an unexplained digestive problem.',
  'Cook plain oats with water, cool them and offer only a little if appropriate. Keep milk, toppings and flavored '
  "mixtures out of the cat's portion."),
 ('catnip',
  'Catnip',
  'caution',
  'Catnip can be used for enrichment, but it can also cause vomiting, diarrhea, stimulation or sedation. ASPCA '
  'classifies the plant as toxic to cats; this is not a reason to treat every small toy exposure as a severe '
  'poisoning.',
  'Use an identifiable enrichment product as directed and supervise it. Remove it after an adverse reaction; ask '
  'your veterinarian about ingestion, concentrated products or swallowed toy parts.')]

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
 'bones': ('Do not feed', 'Do not feed cooked bones: they can lodge, choke or injure a cat.', 'What to do', 'hazards'),
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
 'catnip': ('Caution · digestive effects', 'Catnip may cause vomiting or diarrhea; use supervised enrichment and avoid large ingestion.', 'Use for supervised enrichment', 'produce'),
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

FOOD_SOURCES = {'chocolate': [('Merck Veterinary Manual: chocolate toxicosis',
                'https://www.merckvetmanual.com/toxicology/food-hazards/chocolate-toxicosis-in-animals'),
               ('ASPCA: food hazards',
                'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets')],
 'onions': [('ASPCA: onion', 'https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/onion'),
            ('Merck Veterinary Manual: Allium toxicosis',
             'https://www.merckvetmanual.com/toxicology/food-hazards/garlic-and-onion-allium-spp-toxicosis-in-animals'),
            ('ASPCApro: feline toxic exposures',
             'https://www.aspcapro.org/resource/common-feline-toxic-exposures-and-their-treatment')],
 'garlic': [('ASPCA: garlic',
             'https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/garlic'),
            ('Merck Veterinary Manual: garlic and onion toxicosis',
             'https://www.merckvetmanual.com/toxicology/food-hazards/garlic-and-onion-allium-spp-toxicosis-in-animals')],
 'chives': [('ASPCA: chives',
             'https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/chives'),
            ('Merck Veterinary Manual: Allium plants',
             'https://www.merckvetmanual.com/toxicology/food-hazards/garlic-and-onion-allium-spp-toxicosis-in-animals')],
 'grapes': [('Vet Record 2026: evidence review of grapes and raisins in cats',
             'https://pmc.ncbi.nlm.nih.gov/articles/PMC13543696/'),
            ('FDA: potentially dangerous edible items',
             'https://www.fda.gov/animal-veterinary/animal-health-literacy/potentially-dangerous-items-your-pet'),
            ('2022 cohort: Vitis fruit exposure in dogs and cats',
             'https://pmc.ncbi.nlm.nih.gov/articles/PMC9303671/')],
 'raisins': [('Vet Record 2026: feline grape and raisin evidence',
              'https://pmc.ncbi.nlm.nih.gov/articles/PMC13543696/'),
             ('WSAVA: feeding treats to cats',
              'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf')],
 'alcohol': [('MSD Veterinary Manual: toxicoses from alcohols',
              'https://www.msdvetmanual.com/toxicology/toxicoses-from-household-hazards/toxicoses-from-alcohols-in-animals'),
             ('Pet Poison Helpline: alcohol', 'https://www.petpoisonhelpline.com/poison/alcohol/')],
 'coffee': [('Pet Poison Helpline: caffeine in drinks and concentrated products',
             'https://www.petpoisonhelpline.com/poison/caffeine/'),
            ('Cornell: small-animal toxins including caffeine',
             'https://www.vet.cornell.edu/hospitals/pharmacy/consumer-clinical-care-guidelines-animals/small-animal-toxins')],
 'raw-dough': [('Merck Veterinary Manual: bread dough toxicosis',
                'https://www.merckvetmanual.com/toxicology/food-hazards/bread-dough-toxicosis-in-animals'),
               ('ASPCApro: bread ingestion in pets', 'https://www.aspcapro.org/resource/bread-ingestion-pets')],
 'xylitol': [('2018 clinical study: orally administered xylitol in six cats',
              'https://pubmed.ncbi.nlm.nih.gov/29430681/'),
             ('ASPCApro: cats versus dogs and xylitol',
              'https://www.aspcapro.org/sites/default/files/2020-11/pets-and-kids_apcc_2020_v2.pdf')],
 'avocado': [('ASPCA: species differences in avocado sensitivity',
              'https://www.aspca.org/news/scoop-avocado-and-your-pets'),
             ('FDA: avocado and fruit-pit obstruction',
              'https://www.fda.gov/animal-veterinary/animal-health-literacy/potentially-dangerous-items-your-pet'),
             ('Merck Veterinary Manual: gastrointestinal obstruction',
              'https://www.merckvetmanual.com/digestive-system/surgical-problems-of-the-gastrointestinal-tract-in-small-animals/gastrointestinal-obstruction-in-small-animals')],
 'bones': [('WSAVA: cooked and raw bone risks in cats',
            'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
           ('FDA: bones and gastrointestinal obstruction',
            'https://www.fda.gov/animal-veterinary/animal-health-literacy/potentially-dangerous-items-your-pet'),
           ('Merck Veterinary Manual: gastrointestinal obstruction',
            'https://www.merckvetmanual.com/digestive-system/surgical-problems-of-the-gastrointestinal-tract-in-small-animals/gastrointestinal-obstruction-in-small-animals')],
 'milk': [('ASPCA: dairy and other people-food hazards',
           'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
          ('Cornell: feeding your cat',
           'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
          ('WSAVA: feeding treats to your cat',
           'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
          ('CDC: pet-food safety', 'https://www.cdc.gov/healthy-pets/about/pet-food-safety.html'),
          ('Cornell: vomiting',
           'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'cheese': [('ASPCA: dairy and Allium hazards',
             'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
            ('Cornell: nutrition and supplements',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
            ('WSAVA: treat calories and medical diets',
             'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
            ('Cornell: vomiting',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'yogurt': [('ASPCA: milk and dairy',
             'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
            ('ASPCApro: feline xylitol context',
             'https://www.aspcapro.org/resource/most-common-sleep-aid-toxicities-cats-and-dogs'),
            ('Cornell: feeding your cat',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
            ('WSAVA: treats', 'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
            ('Cornell: vomiting',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'tuna': [('FDA: complete and balanced pet food',
           'https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food'),
          ('Cornell: feeding and fish-product cautions',
           'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
          ('ASPCA: Allium hazards',
           'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
          ('WSAVA: treats', 'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
          ('CDC: pet-food safety', 'https://www.cdc.gov/healthy-pets/about/pet-food-safety.html'),
          ('Cornell: vomiting',
           'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'chicken': [('Cornell: feline nutrition',
              'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
             ('ASPCA: Allium hazards',
              'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
             ('FDA: poultry cooking and food handling',
              'https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling'),
             ('CDC: raw animal-food risks', 'https://www.cdc.gov/healthy-pets/about/pet-food-safety.html'),
             ('Merck: limited homemade diets',
              'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
             ('WSAVA: treats', 'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
             ('Cornell: vomiting',
              'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'cooked-eggs': [('Cornell: feeding your cat',
                  'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
                 ('FDA: egg cooking and food handling',
                  'https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling'),
                 ('Merck: avidin and nutrition',
                  'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
                 ('ASPCA: dairy and seasoning hazards',
                  'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
                 ('WSAVA: treat limits',
                  'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
                 ('Cornell: vomiting',
                  'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'raw-eggs': [('ASPCA: raw eggs',
               'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
              ('Merck: avidin and biotin',
               'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
              ('FDA: cooking eggs', 'https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling'),
              ('FDA: complete and balanced diets',
               'https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food'),
              ('WSAVA: treats', 'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
              ('Cornell: vomiting',
               'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'raw-fish': [('Cornell: raw diets',
               'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
              ('Merck: thiamine and raw-fish enzymes',
               'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
              ('CDC: raw pet-food safety', 'https://www.cdc.gov/healthy-pets/about/pet-food-safety.html'),
              ('FDA: safe food handling', 'https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling'),
              ('WSAVA: treats', 'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
              ('Cornell: vomiting',
               'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'cucumber': [('ASPCA: garden cucumber classification',
               'https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/cucumber'),
              ('ASPCA: Allium hazards',
               'https://www.aspca.org/news/pets-and-produce-top-tips-vegetable-garden-safety'),
              ('WSAVA: treats and individual suitability',
               'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
              ('Merck: digestive signs',
               'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats')],
 'peanut-butter': [('Cornell: feline nutrition',
                    'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
                   ('ASPCApro: feline xylitol context',
                    'https://www.aspcapro.org/resource/most-common-sleep-aid-toxicities-cats-and-dogs'),
                   ('WSAVA: treat budgeting',
                    'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
                   ('Cornell: vomiting',
                    'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'dog-food': [('Merck: differences between feline and canine nutrition',
               'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
              ('FDA: complete-and-balanced claims',
               'https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food'),
              ('Cornell: feeding and supplements',
               'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
              ('WSAVA: treat limits',
               'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
              ('CDC: raw pet-food risks', 'https://www.cdc.gov/healthy-pets/about/pet-food-safety.html'),
              ('Cornell: vomiting',
               'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'ham': [('ASPCA: salty foods and Allium ingredients',
          'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
         ('ACVIM: consensus on feline pancreatitis', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7995362/'),
         ('WSAVA: treat budgeting', 'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
         ('FDA: complete and balanced food',
          'https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food'),
         ('Cornell: vomiting',
          'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'bread': [('ASPCApro: fully baked bread versus raw yeast dough',
            'https://www.aspcapro.org/resource/bread-ingestion-pets'),
           ('WSAVA: cat treat limits',
            'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
           ('ASPCA: ingredient hazards and species distinctions',
            'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets')],
 'banana': [('ASPCA: banana classification',
             'https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/banana'),
            ('Pet Poison Helpline: produce options',
             'https://www.petpoisonhelpline.com/uncategorized/pet-friendly-human-food/'),
            ('VCA: cat treat budgets', 'https://vcahospitals.com/know-your-pet/cat-treats'),
            ('Cornell: feeding and appetite',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
            ('Merck: RER and neutered-cat factor',
             'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
            ('WSAVA: treat ceiling',
             'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf')],
 'apples': [('ASPCA: apple plant hazards',
             'https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/apple'),
            ('Pet Poison Helpline: produce options',
             'https://www.petpoisonhelpline.com/uncategorized/pet-friendly-human-food/'),
            ('Cornell: feeding your cat',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
            ('VCA: cat treats', 'https://vcahospitals.com/know-your-pet/cat-treats'),
            ('Merck: digestive warning signs',
             'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats')],
 'turkey': [('ASPCA: people-food hazards',
             'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
            ('FDA: poultry cooking', 'https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling'),
            ('WSAVA: bones and treat limits',
             'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
            ('Cornell: nutrition',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
            ('Cornell: vomiting',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'salmon': [('Cornell: feline nutrition and supplements',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
            ('FDA: fish cooking and handling',
             'https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling'),
            ('WSAVA: bones and treat limits',
             'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
            ('ASPCA: seasoning hazards',
             'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
            ('FDA: complete and balanced diets',
             'https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food'),
            ('Cornell: vomiting',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'shrimp': [('ASPCA: seasoning hazards',
             'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
            ('FDA: seafood preparation', 'https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling'),
            ('CDC: raw animal-food risks', 'https://www.cdc.gov/healthy-pets/about/pet-food-safety.html'),
            ('Cornell: feline nutrition',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
            ('FDA: complete and balanced food',
             'https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food'),
            ('WSAVA: treats', 'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
            ('Cornell: vomiting',
             'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting')],
 'pumpkin': [('Cornell: urinary obstruction warning',
              'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feline-lower-urinary-tract-disease'),
             ('Merck: intestinal disorders and constipation',
              'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/disorders-of-the-stomach-and-intestines-in-cats'),
             ('Pet Poison Helpline: plain pumpkin',
              'https://www.petpoisonhelpline.com/uncategorized/pet-friendly-human-food/'),
             ('Merck: digestive warning signs',
              'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats')],
 'blueberries': [('VCA: blueberry treats and dietary restrictions',
                  'https://vcahospitals.com/know-your-pet/cat-treats'),
                 ('ASPCA: mixed-food hazards',
                  'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
                 ('Merck: digestive warning signs',
                  'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats'),
                 ('VCA: human foods for training cats (specific fruit examples)',
                  'https://vcahospitals.com/know-your-pet/using-food-and-treats-for-training-cats')],
 'watermelon': [('VCA: seedless watermelon as a treat', 'https://vcahospitals.com/know-your-pet/cat-treats'),
                ('Cornell: water access and diet',
                 'https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat'),
                ('ASPCA: alcohol and mixed-food hazards',
                 'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
                ('Merck: digestive signs',
                 'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats'),
                ('Merck: RER and neutered-cat factor',
                 'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
                ('WSAVA: treat ceiling',
                 'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
                ('VCA: human foods for training cats (specific fruit examples)',
                 'https://vcahospitals.com/know-your-pet/using-food-and-treats-for-training-cats')],
 'strawberries': [('VCA: strawberries among treat options', 'https://vcahospitals.com/know-your-pet/cat-treats'),
                  ('Merck: feline vitamin requirements',
                   'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
                  ('ASPCA: chocolate and dairy hazards',
                   'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
                  ('WSAVA: feline treats',
                   'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
                  ('Merck: digestive signs',
                   'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats'),
                  ('VCA: human foods for training cats (specific fruit examples)',
                   'https://vcahospitals.com/know-your-pet/using-food-and-treats-for-training-cats')],
 'cantaloupe': [('Veterinarian Lauren Jones: cantaloupe',
                 'https://www.petco.com/pet-education/cat/vet-qa/cat-eat-cantaloupe-safety'),
                ('ISFM: feline nutritional requirements', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11107985/'),
                ('ASPCA: mixed-food hazards',
                 'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
                ('Merck: digestive signs',
                 'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats')],
 'carrots': [('Merck: preformed vitamin A in cats',
              'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
             ('RSPCA: carrot preparation for cats', 'https://www.rspca.org.uk/adviceandwelfare/seasonal/christmas'),
             ('ASPCA: garden produce and Alliums',
              'https://www.aspca.org/news/pets-and-produce-top-tips-vegetable-garden-safety'),
             ('Merck: digestive signs',
              'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats')],
 'green-beans': [('Pet Poison Helpline: green beans as an option',
                  'https://www.petpoisonhelpline.com/uncategorized/pet-friendly-human-food/'),
                 ('ISFM: nutritional adequacy', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11107985/'),
                 ('ASPCA: Allium hazards',
                  'https://www.aspca.org/news/pets-and-produce-top-tips-vegetable-garden-safety'),
                 ('WSAVA: feline treats',
                  'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
                 ('VCA: diarrhea in cats', 'https://vcahospitals.com/know-your-pet/diarrhea-in-cats')],
 'peas': [('ASPCA: peas among moderate produce snacks',
           'https://www.aspca.org/news/pets-and-produce-top-tips-vegetable-garden-safety'),
          ('ISFM: feline nutrition and processed starch', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11107985/'),
          ('WSAVA: medical diets and treats',
           'https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf'),
          ('VCA: diarrhea in cats', 'https://vcahospitals.com/know-your-pet/diarrhea-in-cats')],
 'rice': [('ISFM: processed starch and feline requirements', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11107985/'),
          ('VCA: limits of chicken-and-rice diets',
           'https://vcahospitals.com/know-your-pet/bland-diet-instructions-for-dogs-and-cats'),
          ('ASPCA: onion and garlic hazards',
           'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
          ('VCA: diarrhea in cats', 'https://vcahospitals.com/know-your-pet/diarrhea-in-cats')],
 'oatmeal': [('Purina: plain oatmeal, water preparation and small amounts',
              'https://www.purina.com/articles/cat/feeding/can-cats-eat/oatmeal'),
             ('Merck: fiber and nutritional requirements',
              'https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals'),
             ('ASPCA: mixed-food hazards',
              'https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets'),
             ('VCA: diarrhea in cats', 'https://vcahospitals.com/know-your-pet/diarrhea-in-cats')],
 'catnip': [('ASPCA: catnip and possible adverse effects',
             'https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/catnip'),
            ('Merck: feline intestinal foreign objects',
             'https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/disorders-of-the-stomach-and-intestines-in-cats'),
            ('Merck: swallowed string and other objects',
             'https://www.merckvetmanual.com/special-pet-topics/emergencies/minor-injuries-and-accidents')]}

FOOD_EXTRA = {'chocolate': 'Chocolate in a brownie, coating, drink or baking mix still needs assessment. Save the ingredient list '
              'and distinguish the weight of the whole food from the amount of chocolate it contains.',
 'onions': 'Onion can be part of a recipe even when no visible onion pieces remain. Check soup bases, gravies, '
           'seasoning mixtures and foods offered to hide medication.',
 'garlic': 'Garlic powder, garlic salt, seasoned broth and garlic-containing sauces can make an otherwise '
           'plain-looking food unsuitable to share. Read the finished recipe, not just the name of the meat or '
           'vegetable.',
 'chives': 'Fresh chives in an herb pot, chopped garnish and dried chives in a seasoning jar all need to be '
           'identified accurately after an exposure.',
 'grapes': 'A 2026 veterinary evidence review found the cat-specific literature insufficient for a firm toxicity '
           'conclusion. Precautionary avoidance does not mean that kidney failure is an established outcome in every '
           'exposed cat.',
 'raisins': 'Sultanas and many dried currants used in baking are also grape products. Check the package rather than '
            'relying on the color or size of a dried fruit.',
 'alcohol': 'Give the clinic the exact beverage or product name. Beer, spirits, alcohol-filled sweets and fermenting '
            'yeast dough are different descriptions, and a mixed drink may contain additional concerning '
            'ingredients.',
 'coffee': 'Used grounds, tea bags, espresso products and energy supplements belong in the exposure history. A lick '
           'of a diluted drink and access to concentrated caffeine are not interchangeable events.',
 'raw-dough': 'Tell the veterinarian whether yeast was present and whether the dough was raw, proofing, partly baked '
              'or fully baked. Include fillings, toppings and any packaging or utensils that may have been chewed.',
 'xylitol': 'ASPCApro distinguishes the dog poisoning syndrome from possible stomach upset in cats. Read the '
            'complete product label and ask your veterinarian about an accidental ingestion rather than applying a '
            'dog dose chart.',
 'milk': 'Lactose-free milk can still be an incomplete, calorie-containing treat. Pasteurization reduces microbial '
         'risk but does not correct lactose intolerance or establish nutritional completeness.',
 'cheese': 'A lower lactose content does not prove tolerance, and no universal safe cheese portion has been '
           'established for every cat. Flavored spreads may add onion or garlic.',
 'yogurt': 'Plain, unsweetened labeling does not guarantee tolerance. Check all ingredients; yogurt is not a '
           'substitute for a feline probiotic chosen by your veterinary team.',
 'tuna': 'Check the nutritional-adequacy statement on feline tuna foods rather than assuming that every fish product '
         'is complete. A cat eating only human tuna needs a diet review.',
 'raw-fish': 'Thiaminase content varies among fish. A single exposure and a long-term raw-fish diet are different '
             'situations; neither warrants an invented home vitamin dose.',
 'raw-eggs': 'Avidin binds biotin; it is not a claim that a single raw-egg lick causes an immediate deficiency. '
             'Cooking and a complete feline diet address different parts of the feeding question.',
 'bones': 'Tell the clinic the kind of bone, whether it was cooked, its approximate size and whether pieces are '
          'missing. Do not assume that a swallowed bone is safe because it came from an otherwise suitable meat.',
 'dog-food': 'Cats need a feline nutrient profile, not merely a meat ingredient. Adding tuna, egg or an unprescribed '
             'supplement to dog food does not establish a balanced cat diet.',
 'ham': 'A direct claim that fatty table scraps cause pancreatitis in cats is not established. Cats with '
        'pancreatitis or other disease need an individualized feeding plan.',
 'avocado': 'Distinguish flesh, skin, pit and a prepared food such as guacamole. The product description is more '
            'useful than a blanket claim that all avocado exposures have the same feline risk.',
 'peanut-butter': 'Do not infer that peanut butter is needed for feline protein, enrichment or medication. Check '
                  'with the prescribing clinic before using any food to deliver a drug.',
 'bread': 'Check the full recipe before sharing any baked product. Garlic bread, onion loaves, raisin bread and '
          'chocolate-containing products require their own ingredient-specific assessment.',
 'banana': 'Use ripe peeled flesh only, and inspect banana-containing products for other ingredients. No fruit '
           'serving is required when a cat eats a suitable complete diet.',
 'apples': 'Prepare a little clean apple flesh separately from the core and any dessert ingredients. Fruit is '
           'optional and does not replace complete cat food.',
 'chicken': 'Set aside chicken before adding broth, onion, garlic or sauce. Removing skin from a seasoned product '
            'does not establish that the remaining meat is plain.',
 'turkey': 'A seasoned or injected bird is not necessarily plain beneath its skin. Keep carcasses, bones and food '
           'packaging out of reach after the meal.',
 'salmon': 'Smoked, cured, glazed and raw salmon are different products. Their preparation and ingredients cannot be '
           'assessed from the fish name alone.',
 'cooked-eggs': 'Make a separate portion without milk, cheese, butter or seasoning. A whole human breakfast serving '
                "should not be copied into a cat's treat allowance.",
 'shrimp': 'Shrimp vary in size, so a universal shrimp-count serving is misleading. Keep garlic butter, cocktail '
           "sauce, brine and fried coatings out of the cat's portion.",
 'pumpkin': 'Distinguish an optional taste from a veterinarian-directed diet change. Choose plain puree, keep the '
            'product and measurement consistent if prescribed, and record whether normal food intake changes.',
 'blueberries': 'Wash and split or flatten a small amount so it is easy to supervise. Avoid sweetened or baked '
                'blueberry products unless every other ingredient has been assessed.',
 'watermelon': 'Remove rind and seeds, offer a soft small piece separately from fruit salads, and keep ordinary '
               'drinking water available.',
 'strawberries': 'Wash the fruit, remove the top and offer a little flesh separately from dairy desserts or '
                 'chocolate coatings. Leaf removal is a preparation choice, not a claim of apple-like cyanide '
                 'toxicity.',
 'cantaloupe': 'Prepare soft flesh separately from rind, seeds and other fruit-salad ingredients. Interest in the '
               'smell does not establish a nutritional need.',
 'carrots': 'Cook until soft, cool and cut into small pieces. Reserve it before adding glazes, stock, onions or '
            'garlic; do not use vegetables to dilute a complete diet.',
 'cucumber': 'Wash, prepare a small manageable piece and offer it calmly on a dish. Avoid pickles, garlic dressings '
             'and using cucumber to frighten a cat.',
 'green-beans': 'Use tender chopped beans without sauces or onion toppings. Check canned and frozen products for '
                'added ingredients, and keep vegetables as extras rather than bulk meal replacements.',
 'peas': 'Mash or split a small amount and keep sauces, pods and packaging away from the dish. Check medical feeding '
         'plans before adding an unfamiliar treat.',
 'rice': 'Distinguish a few plain grains from a repeated rice-based ration. Check broth and sauces, and do not '
         'assume a homemade chicken-and-rice diet is complete.',
 'oatmeal': 'Assess the cooked grain separately from breakfast toppings. Fiber content does not establish a '
            'treatment amount, and the added water changes serving weight.',
 'catnip': 'Catnip is optional enrichment rather than food or medicine. Different preparations and toy materials '
           'need separate assessment, and no response needs to be forced.'}

# Food-specific detail sections (trusted HTML). Priority foods get deeper original notes.
FOOD_DETAIL = {'chocolate': [('Why a cocoa label matters more than the size of a bite',
                '<p>A missing piece of chocolate is not a useful dose description by itself. A square from a baking '
                'bar, a crumb of brownie and a lick of chocolate frosting contain different ingredients and '
                'different amounts of cocoa. <a '
                'href="https://www.merckvetmanual.com/toxicology/food-hazards/chocolate-toxicosis-in-animals">Merck '
                'Veterinary Manual</a> identifies theobromine and caffeine as the principal toxic compounds. Their '
                'effects include stimulation of the heart and nervous system; this is a poisoning concern rather '
                'than simply an unsuitable snack.</p><p>Look for the original package while another person contacts '
                'the clinic. Record the brand, product name and cocoa percentage if printed. Keep a separate '
                'estimate for the total food eaten and the chocolate component. If a recipe used several kinds of '
                'chocolate, send the recipe rather than treating every gram of cake as a gram of cocoa. A clear '
                'photograph of both sides of the wrapper can be more useful than a remembered description.</p>'),
               ('Dark, milk and white chocolate are different exposure questions',
                '<p>Darker products and cocoa powder usually contain more methylxanthines than milk chocolate, '
                'according to <a '
                'href="https://www.merckvetmanual.com/toxicology/food-hazards/chocolate-toxicosis-in-animals">Merck\'s '
                'chocolate review</a>. White chocolate is a much smaller source of those compounds. This comparison '
                'helps a professional assess an accident; it does not make white chocolate an appropriate cat treat '
                'or let an owner rule out problems from an unknown mixed dessert.</p><p>For a filled confection, '
                'identify the filling as well as the coating. Coffee flavoring, liqueur and other ingredients '
                'deserve separate attention. Compare our <a href="/can-cats-eat/coffee/">coffee guide</a> and <a '
                'href="/can-cats-eat/alcohol/">alcohol guide</a> if either appears in the recipe. Sugar-free '
                'labeling also warrants checking the sweetener, but do not assume the well-known dog response to '
                'xylitol is established in cats. Our <a href="/can-cats-eat/xylitol/">xylitol evidence page</a> '
                'explains that distinction.</p>'),
               ('A quiet cat does not settle the question',
                '<p>The <a '
                'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
                'food-hazard guidance</a> describes gastrointestinal upset, abnormal activity, heart-rhythm changes, '
                'tremors and seizures after methylxanthine exposure. An owner cannot reliably measure a heart rhythm '
                'from watching a resting cat. Report behavior changes and anything actually observed, rather than '
                'deciding that an apparently comfortable animal must be unaffected.</p><p>Separate a witnessed '
                'ingestion from a suspected one. For example, a torn wrapper and a missing truffle leave uncertainty '
                'about who ate it and how much; tell the veterinary team exactly that. Do not delay the call while '
                'reconstructing a perfect history. If the cat is trembling, collapses or has difficulty breathing, '
                'seek emergency care immediately. Keeping a short written timeline prevents different household '
                'members from giving contradictory estimates when the clinic asks follow-up questions.</p>'),
               ('Why the calorie calculator cannot clear chocolate',
                '<p>The <a href="/cat-calorie-calculator/">CatCalc calorie calculator</a> estimates food energy '
                'needs. It does not evaluate theobromine, caffeine, packaging or any toxic exposure. A food fitting '
                'inside a daily calorie allowance says nothing about whether its ingredients are safe. Chocolate is '
                'therefore excluded from intentional feeding regardless of whether a small amount could fit the '
                'arithmetic.</p><p>Avoid using a dog chocolate calculator as a feline clearance certificate. Such '
                'tools may make assumptions about products and species that do not match the accident. Share any '
                'calculation already made with the veterinarian, alongside the packaging, and let the clinical team '
                'determine its relevance. The <a href="/guides/how-catcalc-rates-human-foods/">food-rating '
                'method</a> distinguishes poisoning from excess calories because those are separate questions. No '
                'online portion estimate should postpone professional advice after an exposure.</p>'),
               ('Make the baking area inaccessible before ingredients come out',
                '<p>Chocolate prevention works best as a kitchen routine. Put bars, cocoa tins and opened baking '
                'bags behind a closed cupboard door. During baking, clear drips and scraps as they occur, then put '
                'wrappers in a bin the cat cannot open. A high counter is still accessible to many cats, so height '
                'alone should not be the storage plan.</p><p>Ask guests to keep chocolate gifts inside their bags or '
                'in the cupboard rather than on a low table. When children unwrap sweets, provide a separate bowl '
                'for empty wrappers and remove it promptly. If you want to include a cat in a celebration, use part '
                'of its normal cat-food allowance or an appropriate cat treat in its own dish. Keep the human '
                "dessert and the cat's food physically separate so nobody mistakes supervised sharing for permission "
                'to offer chocolate.</p><p>Keep baking cocoa separate from flour so an opened ingredient bag cannot '
                'be mistaken for a harmless spill.</p>')],
 'onions': [('The problem is red blood cell injury',
             '<p>Onion poisoning is different from the digestive upset that can follow an unfamiliar meal. <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/onion">ASPCA\'s '
             'onion entry</a> identifies cats as a susceptible species and lists destruction of red blood cells '
             "among the effects. The resulting anemia reduces the blood's ability to carry oxygen. It is therefore "
             'misleading to judge an onion-containing meal only by whether the cat vomited soon afterward.</p><p>The '
             '<a '
             'href="https://www.merckvetmanual.com/toxicology/food-hazards/garlic-and-onion-allium-spp-toxicosis-in-animals">Merck '
             'Allium review</a> explains that concerning exposures include raw, cooked, dehydrated and granulated '
             'onion. Cooking a sauce until the onion disappears does not remove the underlying concern. Keep that '
             'distinction in mind when a cat eats a spoonful of gravy or soup rather than a recognizable onion ring. '
             'What matters for the consultation is the ingredient history, not whether the original vegetable can '
             'still be picked out of the dish.</p>'),
            ('Broth and baby food need the same ingredient check as leftovers',
             '<p>Broth sometimes becomes an improvised way to tempt a cat that is not eating. Before offering any '
             'human broth, inspect the entire ingredient list. Onion, onion powder and onion-containing soup '
             'concentrates can be less obvious than a pile of chopped onion. The <a '
             'href="/can-cats-eat/garlic/">garlic page</a> covers another Allium that may appear in the same '
             'product; a product without onion can still contain garlic.</p><p>Do the same check for baby food or a '
             'soft food intended to hide a tablet. Ask the prescribing veterinarian what can be used with that '
             'medicine rather than assuming a smooth meat puree is suitable. Save the container if the food has '
             'already been eaten. Homemade broth needs a recipe review too: straining out solids does not turn a '
             'seasoned stock into the plain meat discussed on our <a href="/can-cats-eat/chicken/">cooked-chicken '
             'page</a>.</p>'),
            ('Small repeated offerings belong in the history',
             '<p>An exposure history is more useful when it includes the whole recent feeding routine. If someone '
             'has been adding a little soup to meals, record how often, approximately how much, and which soup it '
             'was. Do not report only the most recent spoonful because earlier offerings seem irrelevant. <a '
             'href="https://www.aspcapro.org/resource/common-feline-toxic-exposures-and-their-treatment">ASPCApro\'s '
             'feline toxic-exposure guidance</a> discusses onion-containing food as a specific concern in '
             'cats.</p><p>There is no household measuring trick that reliably turns a mixed recipe into a safe '
             'feline onion allowance. A teaspoon of powder and a teaspoon of cooked onion are not interchangeable '
             'ingredient descriptions. Avoid deciding that a powder is harmless because its volume is small. Give '
             'the veterinary team the best estimate available and explain what cannot be measured. That is more '
             'useful than making a confident but unsupported calculation from an online toxic-dose table.</p>'),
            ('Delayed weakness is a reason to reconnect with the clinic',
             '<p><a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/onion">ASPCA</a> '
             'lists weakness, blood in the urine, an increased heart rate and panting among onion-related signs. <a '
             'href="https://www.merckvetmanual.com/toxicology/food-hazards/garlic-and-onion-allium-spp-toxicosis-in-animals">Merck</a> '
             'also describes delayed anemia after Allium ingestion. Contact the clinic promptly about pale gums, '
             'unusual weakness, collapse or breathing changes. These observations require professional assessment; '
             'they do not prove onion poisoning or exclude another illness.</p><p>Ask the veterinarian whether '
             'rechecks or monitoring are needed and follow the plan for that exposure. An uneventful first evening '
             'does not, by itself, answer the later blood-cell question. Keep the product packaging and the original '
             'timeline until the team says they are no longer needed. If different people care for the cat, write '
             'down who is responsible for observing meals and behavior so a change is not missed during a shift '
             'between family members.</p>'),
            ('A practical rule for shared meals',
             '<p>Set aside any intended cat treat before onion or other seasoning enters the pan. Once a dish '
             'contains onion, do not offer a supposedly clean piece from the same sauce. For garnish-heavy dishes, '
             "serve the cat's appropriate food in a separate bowl before the human meal begins; this reduces the "
             'chance of someone sharing from a finished plate.</p><p>The same kitchen rule applies to <a '
             'href="/can-cats-eat/chives/">chives</a> and garlic, although those ingredients deserve their own '
             'labels when reporting an accident. Teach visitors the ingredient names instead of merely saying the '
             'cat cannot have spicy food: onion need not taste hot. Our <a '
             'href="/guides/how-catcalc-rates-human-foods/">ratings guide</a> explains why this is a poisoning '
             'category rather than a portion-control issue. A daily calorie budget never creates an allowance for '
             'onion, and it should not be used to justify a trial serving.</p>')],
 'garlic': [('Garlic is not a feline wellness supplement',
             '<p>Human claims about garlic do not establish a benefit or a safe supplement dose for cats. <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/garlic">ASPCA '
             'lists garlic as toxic to cats</a> and identifies red blood cell damage as a possible effect. That is a '
             "reason to avoid adding cloves, powders or home-made garlic preparations to a cat's meals, even when "
             'the intention is to improve health rather than share a snack.</p><p>This also applies to recipes '
             "circulated as natural flea prevention. A food ingredient's plant origin does not demonstrate that it "
             "is an appropriate parasite-control product. Use a veterinarian's cat-specific recommendations for "
             'parasites and nutrition. If garlic has already been added to food, give the clinic the actual '
             'ingredient, preparation and feeding history. Do not describe it only as an herbal supplement, since '
             'that wording hides the information needed to evaluate the exposure.</p>'),
            ('Powder changes the way an accident is described',
             '<p>The <a '
             'href="https://www.merckvetmanual.com/toxicology/food-hazards/garlic-and-onion-allium-spp-toxicosis-in-animals">Merck '
             'Veterinary Manual Allium review</a> includes concentrated forms among concerning exposures. Garlic '
             'powder in a seasoning blend deserves its own entry on the ingredient list; it should not be treated as '
             'equivalent to the same volume of cooked vegetable. This page deliberately provides no spoon-based '
             'safety limit for either form.</p><p>When calling about seasoned food, read the label rather than '
             "guessing which garlic ingredient was used. Keep the blend's container as well as the food package. If "
             'a recipe calls for garlic paste, a marinade or a stock cube, photograph those labels too. In a '
             'restaurant dish, report that the recipe is unknown and ask the restaurant for the ingredient list '
             'while someone else speaks to the clinic. Uncertainty is a useful part of the history when it is stated '
             'honestly.</p>'),
            ('Plain-looking chicken can still contain garlic',
             '<p>A piece of meat with no sauce on its surface is not necessarily unseasoned. Garlic may have been '
             'part of a marinade, cooking liquid or rub. Our <a href="/can-cats-eat/chicken/">plain cooked chicken '
             'guide</a> and <a href="/can-cats-eat/turkey/">turkey guide</a> refer to separately prepared, '
             "unseasoned meat, not a rinsed portion of a finished human recipe. Plan the cat's food before seasoning "
             'the human dish.</p><p>Garlic bread creates the same problem in a different form. Removing a visible '
             'topping does not establish how much garlic remains in the spread or bread. Use the <a '
             'href="/can-cats-eat/bread/">bread page</a> for the distinction between plain baked bread and '
             'ingredient-rich products. If the cat eats a garlic-containing item, describe the complete food to the '
             'veterinarian: bread, spread, cheese, packaging and any other material swallowed can all be relevant to '
             'the consultation.</p>'),
            ('What changes should prompt another call?',
             '<p><a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/garlic">ASPCA\'s '
             'garlic entry</a> includes vomiting, weakness, blood in urine and abnormal breathing or heart-rate '
             'signs. These symptoms warrant veterinary attention after an exposure. Collapse or breathing difficulty '
             'calls for emergency care. A cat appearing normal immediately afterward is not a reason to cancel the '
             'initial call, because Allium-related blood-cell injury may become apparent later.</p><p>Avoid relying '
             "on the cat's willingness to eat a favorite treat as a home test. Tell the team about normal as well as "
             'abnormal behavior, and ask what observations they want recorded. Mention any recent garlic-containing '
             'meals, not just the meal that triggered concern today. Keep the timeline factual: when the food was '
             'accessible, when ingestion was witnessed, and when each sign was first noticed. That information is '
             'more useful than a label such as acting strange.</p>'),
            ('One family of ingredients, several household routes',
             '<p>Garlic shares an Allium concern with <a href="/can-cats-eat/onions/">onions</a> and <a '
             'href="/can-cats-eat/chives/">chives</a>, but the routes into a cat\'s mouth often differ. Onion may be '
             'visible in a casserole; garlic may be hidden in powder, butter or concentrated stock; chives may be a '
             'final garnish. Knowing all three names helps prevent a well-meaning cook from replacing one hazardous '
             'ingredient with another.</p><p>Keep spice jars and open seasoning packets away from preparation areas '
             'the cat can reach. Wipe up garlic-butter smears before letting a cat into the kitchen, and close the '
             'bin after disposing of takeout containers. Ask anyone feeding the cat to check before offering '
             "leftovers, including foods used for pills. A simple household agreement to use the cat's own food for "
             'rewards avoids having to assess every sauce and seasoning at the table.</p>')],
 'grapes': [('What the feline evidence actually says',
             '<p>Grapes are a useful example of why a cat page should identify the species behind a warning. A <a '
             'href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13543696/">2026 Vet Record evidence review</a> '
             'concluded that the available research could not firmly establish whether grapes or raisins are toxic '
             'to cats. That uncertainty does not turn them into recommended treats, but it does mean that a dog '
             'kidney-poisoning statement should not be repeated as a proven feline fact.</p><p>The practical choice '
             'is straightforward: do not offer grapes, and ask a veterinarian about an accidental ingestion. In that '
             "conversation, distinguish what is known about the food from what is unknown about the cat's response. "
             'Our <a href="/guides/how-catcalc-rates-human-foods/">rating method</a> uses an evidence-limited label '
             'for this reason. It is a precautionary feeding decision, not a claim that feline risk has been '
             'precisely measured.</p>'),
            ('Why a small study cannot supply a safe grape count',
             '<p>The <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9303671/">2022 exposure cohort</a> discusses '
             'a small group of exposed cats, many of which received treatment. Those circumstances limit what can be '
             'inferred about untreated animals. A lack of observed kidney injury in that group is not a validated '
             'serving recommendation for all cats, different grape products or future exposures.</p><p>Avoid '
             "converting a reassuring anecdote into a household experiment. A friend's cat remaining well after "
             'stealing fruit does not tell you whether your own cat should be monitored or examined. Equally, do not '
             'tell a worried owner that one grape inevitably causes feline kidney failure. Both claims go beyond the '
             'evidence. A useful report to the clinic states what was eaten, what is uncertain and what the cat is '
             'doing now; the professional can then decide how to manage that particular exposure.</p>'),
            ('The fruit bowl may contain more than grapes',
             '<p>Fresh grapes can appear loose on a table, mixed into fruit cups or rolled under furniture. When '
             'reporting an accident, identify the actual fruit rather than calling the whole mixture a fruit salad. '
             'Mention any other ingredients and whether a stem, container or wrapping is also missing. Keep the '
             'label of a prepared product so the team can distinguish the fruit from its accompanying '
             'ingredients.</p><p>The <a href="/can-cats-eat/raisins/">raisin page</a> addresses dried grapes in a '
             'separate household context. A raisin loaf, trail mix and a fresh grape bunch need different product '
             'descriptions even though the fruit is related. If you choose an optional fruit treat in the future, '
             'read its own preparation notes, such as <a href="/can-cats-eat/watermelon/">watermelon flesh</a> or <a '
             'href="/can-cats-eat/blueberries/">blueberries</a>. A permitted ingredient elsewhere does not clear '
             'every component of a mixed bowl.</p>'),
            ('Use a monitoring plan from the clinic',
             '<p>The <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13543696/">Vet Record review</a> recommends '
             'close observation of exposed cats so emerging illness can be recognized and addressed. Contact the '
             'veterinarian promptly to agree what that means for your cat rather than borrowing a dog treatment '
             'timetable. If vomiting, appetite loss, unusual lethargy or changes in drinking or urination occur, '
             'report them. Collapse, breathing difficulty or other severe illness warrants emergency care regardless '
             'of which food was involved.</p><p>Ask who to contact overnight and whether any examination or '
             "follow-up is advised. Record the approximate time of access, amount missing, cat's current weight and "
             'any pre-existing disease or medication. If the estimate changes because a grape is later found under a '
             'chair, pass that on. A revised factual account is more helpful than sticking with the first number out '
             'of embarrassment.</p>'),
            ('Keep uncertainty out of the snack routine',
             '<p>Choose a simple storage arrangement that prevents repeat access: refrigerate grapes in a closed '
             "container, clear children's snack bowls and check the floor after washing a bunch. Ask visitors to "
             'keep fruit away from the cat instead of relying on the animal to ignore it. A cat batting a grape '
             'around also makes it harder to know later whether it was eaten.</p><p>There is no need to find a '
             "feline nutritional role for grapes. Appropriate rewards can come from the cat's ordinary complete food "
             'allowance, avoiding the fruit question entirely. The <a href="/cat-calorie-calculator/">calorie '
             'calculator</a> can help organize a normal feeding budget, but it cannot predict grape toxicity or '
             'replace an exposure consultation. Decide food safety before budgeting a snack; a low calorie count '
             "never resolves uncertainty about an ingredient's effect on cats.</p><p>The <a "
             'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/potentially-dangerous-items-your-pet">FDA '
             'household-hazard list</a> also includes grapes and raisins among foods to keep away from pets; it is a '
             'prevention list, not a feline dose study.</p>')],
 'raisins': [('Start with the package, not a guessed fruit count',
              '<p>A raisin exposure often begins with a torn bag of trail mix or a missing piece of cake. Keep the '
              'packaging and write down how much of the entire product is missing. If you saw only one raisin eaten '
              'but the cat had access to an open bag, distinguish the witnessed amount from the possible amount. '
              'That detail matters more than making an exact count from incomplete evidence.</p><p>The <a '
              'href="/can-cats-eat/grapes/">fresh-grape page</a> explains the related feline evidence question. <a '
              'href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13543696/">Vet Record\'s 2026 review</a> found too '
              'little cat-specific research for a firm conclusion about toxicity. CatCalc therefore does not publish '
              'a safe number of raisins or claim that every exposed cat will develop kidney failure. The appropriate '
              'next step is individual veterinary advice, with the product and circumstances clearly described.</p>'),
             ('Baking does not simplify a mixed-food exposure',
              '<p>Raisin bread, fruitcake and oatmeal cookies are mixtures, so the consultation should cover the '
              'recipe as well as the dried fruit. Ask whether chocolate, coffee, alcohol or Allium ingredients were '
              'included. Describe sugar-free sweeteners accurately instead of using a single generic label for all '
              'of them. Our <a href="/can-cats-eat/chocolate/">chocolate guide</a> and <a '
              'href="/can-cats-eat/xylitol/">xylitol page</a> separate those issues and explain why a canine warning '
              'cannot always be pasted onto cats.</p><p>Do not assume that the loaf is ordinary bread after visible '
              'raisins have been pulled out. The remaining portion cannot be assessed merely from its appearance. '
              'When baking at home, keep the recipe and ingredient containers until the food is put away. For a '
              'purchased cake, a photograph of the ingredient panel is preferable to a flavor name such as cinnamon '
              'cake, which may omit the dried fruit entirely.</p>'),
             ('Sultanas and currants need accurate names',
              '<p>The word raisin may not be printed on every grape-containing snack. Sultanas and some baking '
              'currants are dried grape products. Other fruits also carry the common name currant, making a package '
              'label or botanical identification more useful than a remembered name. The <a '
              'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA cat-treat '
              'resource</a> specifically groups raisins, currants and sultanas among ingredients to '
              'avoid.</p><p>When a child or visitor says the cat ate a berry, ask to see the original snack bag. Do '
              'not turn an uncertain identification into a confident answer during a phone consultation. Record the '
              'brand and product name, and tell the clinician whether a paper cup, plastic wrapper or part of a '
              'container may also have been swallowed. A dried-fruit question can involve a second problem from the '
              'packaging, so keep those observations separate and report both.</p>'),
             ('Observation is a clinical plan, not an internet waiting period',
              '<p>The <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13543696/">2026 feline evidence '
              'evaluation</a> supports close observation after ingestion, while emphasizing the limits of available '
              'research. Ask your veterinarian what follow-up fits this particular cat. A dog-focused kidney-injury '
              'timeline is not an established feline schedule, and a normal first meal does not substitute for the '
              'plan the clinic recommends.</p><p>Report vomiting, refusal of food, unusual tiredness or a change in '
              'normal drinking or litter-box habits if they occur. Those signs are not specific enough to diagnose a '
              'raisin effect at home. Tell the team whether the cat has existing kidney disease or other health '
              'problems, and which medications it takes. If a symptom appears after an earlier call, reconnect with '
              'the clinic rather than assuming the first conversation covered every later change. Severe '
              'deterioration should be handled as an emergency regardless of the suspected ingredient.</p>'),
             ('Prevent the repeat accident at the point of access',
              '<p>Dried fruit is easy to leave in several rooms: breakfast cereal at the table, a lunchbox in a '
              'backpack, a baking bowl on the counter and a snack bag beside a sofa. Choose closed storage for each '
              'location instead of treating the pantry alone as the problem. Clear dropped pieces after serving '
              "children and put empty wrappers into a closed bin.</p><p>For reward feeding, use the cat's own food "
              'or a suitable cat treat rather than sampling from a human snack mix. A tiny calorie contribution is '
              'not a safety assessment. The <a href="/cat-calorie-calculator/">calorie calculator</a> is for feeding '
              'estimates, whereas the <a href="/guides/how-catcalc-rates-human-foods/">food-rating guide</a> '
              'explains the ingredient decision. Keeping these two questions separate avoids the mistaken idea that '
              'a food becomes appropriate just because there is space for it inside a daily energy budget.</p>')],
 'xylitol': [('Separate a dog warning from a feline conclusion',
              '<p>Xylitol is a sugar substitute used in some gums, sweets and other household products. Its '
              'well-known dog poisoning syndrome is not automatically a cat diagnosis. A <a '
              'href="https://pubmed.ncbi.nlm.nih.gov/29430681/">published feline study</a> tested six healthy cats '
              'and did not find the toxic pattern expected from dog experience. That is useful species-specific '
              'evidence, but the small group does not answer every question about ill cats, repeated access or '
              'different commercial mixtures.</p><p>The practical feeding advice is still to avoid offering xylitol '
              "products. They have no necessary role in a cat's diet, and an ingredient label may contain other "
              'substances that need attention. This is why the page uses a limited-evidence warning rather than '
              'promising safety or predicting canine-style poisoning. Our <a '
              'href="/guides/how-catcalc-rates-human-foods/">rating method</a> explains how an uncertainty label '
              'differs from a firmly established feline toxin.</p>'),
             ('What the ASPCA cat note does and does not imply',
              '<p>An <a '
              'href="https://www.aspcapro.org/sites/default/files/2020-11/pets-and-kids_apcc_2020_v2.pdf">ASPCApro '
              'household-safety handout</a> distinguishes low blood sugar and liver failure in dogs from possible '
              'stomach upset in cats. A reader should not merge those species descriptions into a single claim about '
              'all pets. Equally, a reassuring statement about one ingredient is not a clearance of a swallowed gum '
              'packet or a chocolate-containing sweet.</p><p>If a cat vomits, becomes unusually lethargic or shows '
              'another concerning change after eating a product, contact a veterinarian regardless of what the '
              'xylitol evidence suggests. A symptom may relate to another ingredient, a swallowed object or an '
              'unrelated illness. Do not decide that it must be xylitol poisoning, and do not decide that the '
              'absence of a known feline xylitol syndrome makes the symptoms unimportant. Identify the whole '
              'exposure and let the clinician assess it.</p>'),
             ('Check the whole jar, tube or packet',
              '<p>Bring the original package to the consultation, including both the ingredient panel and the '
              'quantity information. Xylitol may be marketed as birch sugar, but a marketing name is not a '
              'substitute for an ingredient list. If you cannot identify the sweetener, report the product as '
              'unknown instead of guessing from the phrase sugar-free.</p><p>Mixed foods need their own assessment. '
              'A sweet containing <a href="/can-cats-eat/chocolate/">chocolate</a> or a product with <a '
              'href="/can-cats-eat/coffee/">caffeine</a> should not be judged only by its xylitol content. A jar of '
              '<a href="/can-cats-eat/peanut-butter/">peanut butter</a> raises portion and ingredient questions even '
              'when xylitol is absent. For toothpaste, medicine or another non-food product, tell the veterinarian '
              'exactly what it is used for. Do not treat a small amount of a dental product as equivalent to the '
              'same amount of a plain food ingredient.</p>'),
             ('Avoid turning research doses into a feeding instruction',
              '<p>The <a href="https://pubmed.ncbi.nlm.nih.gov/29430681/">feline study</a> describes controlled '
              'administration and observation of healthy animals. Research amounts should not be copied into a '
              'household safe-dose table. The study was designed to investigate a question, not to establish a '
              'recommended serving of gum or sweets for cats. It also cannot tell an owner how much xylitol was '
              "present in an unknown portion of a commercial product.</p><p>When asking for help, give the cat's "
              'weight, product name, estimated amount and time. State whether a wrapper or plastic container was '
              'chewed and whether any of it is missing. If the cat had access while you were away, give the possible '
              'time range. An honest account of uncertainty is more useful than a precise number produced by '
              'multiplying a guessed concentration by a guessed amount.</p>'),
             ('Use the label lesson without making sweets part of feeding',
              '<p>Store gum, mints and dental products where the cat cannot reach them, including inside handbags or '
              'backpacks that might otherwise be left open. Keep tablets and liquid medicines in their original '
              'containers. This makes accidental exposures less likely and preserves the information needed if '
              'something is chewed. Remove empty packets promptly rather than leaving them beside a snack '
              "bowl.</p><p>For routine rewards, choose the cat's own food or a suitable cat treat. The <a "
              'href="/cat-calorie-calculator/">calorie calculator</a> can help account for ordinary feeding energy, '
              'but it is not a toxicology tool. A sugar-free label does not prove a snack is appropriate, just as '
              'the absence of xylitol does not prove every other ingredient is safe. Make ingredient suitability the '
              'first decision and calorie budgeting the second, without using either one as a substitute for '
              'veterinary advice after an accident.</p>')],
 'milk': [('Why the saucer tradition is misleading',
           '<p>A cat may eagerly lap milk without digesting it comfortably. Lactose is the sugar in milk; lactase is '
           'the intestinal enzyme needed to break it down. <a '
           'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
           'explains that limited lactase activity can allow dairy to cause diarrhea and digestive upset</a>. '
           'Enjoying the taste therefore tells you little about tolerance. A cat that seemed comfortable after one '
           'stolen lick has not passed a lifelong milk test, and a daily saucer is not an appropriate reward '
           'routine.</p><p>This is different from saying that every trace of milk is a veterinary emergency. If an '
           'otherwise well adult cat steals a lick of plain pasteurized milk, remove the saucer and watch its '
           'behavior and litter box. Describe the actual product if you call the clinic: cow’s milk, cream, a '
           'sweetened drink and a coffee creamer are not interchangeable exposures.</p>'),
          ('An orphaned kitten needs a different product',
           '<p>The familiar picture of a kitten drinking cow’s milk confuses two nutritional situations. An unweaned '
           'kitten needs an appropriate milk-replacement feeding plan, whereas an adult cat should receive a '
           'complete diet for its life stage. <a '
           'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
           'describes the many nutrients that feline diets must supply</a>; simply supplying white liquid does not '
           'meet that standard. Contact a veterinarian or an experienced rescue working with a veterinarian for an '
           'orphan’s formula, feeding method, frequency and growth checks.</p><p>Do not use lactose-free human milk, '
           'diluted cream, evaporated milk or a homemade kitchen mixture as a replacement selected from this '
           'article. Removing lactose changes one ingredient; it does not establish the correct balance for growth. '
           'Our <a href="/guides/kitten-first-weeks-checklist/">kitten checklist</a> is an organizing aid for '
           'arranging care, rather than a hand-rearing recipe.</p>'),
          ('Lactose-free does not mean unrestricted',
           '<p>A product sold as cat milk may have reduced lactose, but read whether it is a complementary treat or '
           'a complete food. Its calories still belong in the day’s total, and its label does not make it a required '
           'supplement. The <a href="/guides/how-to-read-cat-food-labels/">cat-food label guide</a> explains why a '
           'nutrient claim on the front of a package is less useful than the nutritional-adequacy statement and '
           'feeding information.</p><p><a '
           'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA recommends '
           'that treats contribute no more than 10% of daily calories</a>, with additional restrictions possible for '
           'medical diets. That ceiling covers all extras together, including milk, lickable treats and pieces used '
           'for medication. Use the <a href="/cat-calorie-calculator/">calorie calculator</a> as a starting '
           'estimate, then follow your own veterinarian’s target. There is no reason to spend that allowance on a '
           'drink that repeatedly causes loose stools.</p><p>For a household that already buys a cat-milk treat, '
           'write the opened date on the container and follow the manufacturer’s refrigeration and use instructions. '
           'Do not top an old saucer up with fresh milk. Measuring a portion into a clean dish makes both its intake '
           'and any change in tolerance easier to describe accurately to the veterinary team.</p>'),
          ('Milk drinks bring their own ingredient list',
           '<p>Chocolate milk is a chocolate exposure as well as a dairy exposure. Coffee drinks can contain '
           'caffeine; flavored creamers can contain several ingredients that are absent from plain milk. Read the '
           'container rather than assuming that the pale color makes a drink harmless. The <a '
           'href="/can-cats-eat/chocolate/">chocolate page</a> and <a href="/can-cats-eat/coffee/">coffee page</a> '
           'explain why those ingredients require prompt professional advice.</p><p>Raw milk is a separate '
           'food-safety concern. <a href="https://www.cdc.gov/healthy-pets/about/pet-food-safety.html">CDC advises '
           'against raw pet food and unpasteurized milk because they can carry harmful germs</a>. Pasteurization '
           'addresses a microbial hazard; it does not remove lactose or turn milk into balanced cat food. Keep '
           'drinking glasses out of reach and use fresh water as the normal drink. If a cat consistently prefers '
           'milk while avoiding water or regular meals, discuss the underlying feeding problem rather than '
           'increasing the saucer.</p>'),
          ('When the problem is more than a messy litter box',
           '<p>Stop offering milk if it is followed by digestive upset. Record the quantity, time, product and any '
           'other recent diet change; that history helps the clinic distinguish an exposure from an unrelated '
           'illness. Do not keep challenging a symptomatic cat with progressively smaller portions to prove that '
           'dairy is responsible.</p><p><a '
           'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell '
           'advises veterinary evaluation for vomiting accompanied by weakness, lethargy, reduced appetite, blood or '
           'diarrhea</a>. A kitten, an older cat with weight loss, or a cat already receiving treatment deserves '
           'advice suited to its circumstances. Use our <a href="/guides/senior-cat-weight-and-appetite/">senior '
           'weight and appetite guide</a> to prepare observations for an appointment. Milk does not treat '
           'dehydration or restore appetite safely by itself, and an online article cannot determine how much fluid '
           'a sick cat needs.</p>')],
 'cheese': [('The cheese wrapper is a better guide than the cheese name',
             '<p>Cheese is a broad category, not a single feline snack. A slice, grated topping, soft spread and '
             'processed sauce can differ substantially in ingredients and calories. Before sharing anything, check '
             'the actual package and decide whether it contains a seasoning or flavor that changes the question. A '
             'product described as cheddar-flavored may include several ingredients besides cheese; a restaurant '
             'sauce may have no ingredient label available at all.</p><p>Dairy also has a tolerance problem '
             'independent of flavorings. <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
             'identifies milk and dairy as possible causes of diarrhea and digestive upset because pets have limited '
             'lactase</a>. Some cheeses contain less lactose than milk, but that fact cannot predict an individual '
             'cat’s response. A cat that likes the smell is not demonstrating that its intestine will tolerate a '
             'serving.</p>'),
            ('Calcium does not make cheese a necessary supplement',
             '<p>It is easy to reason that cheese contains a useful nutrient, so adding cheese must improve the '
             'diet. Feline nutrition depends on amounts and proportions across the whole ration. <a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
             'notes that complete diets already supply required nutrients and that extra vitamins or minerals can be '
             'harmful</a>. A cat eating an appropriate complete food does not need a cheese topping to make its '
             'bones stronger.</p><p>Neither should cheese be used to make an unbalanced homemade meat diet complete. '
             'Adding an arbitrary dairy serving does not establish the required mineral balance. If the main diet is '
             'homemade, a veterinarian with nutrition expertise should formulate it. See the <a '
             'href="/guides/how-to-read-cat-food-labels/">cat-food label guide</a> for distinguishing a food '
             'intended as a sole diet from a supplementary snack. Cheese is, at most, an optional extra for a cat '
             'whose own diet allows it.</p>'),
            ('A tiny reward still occupies the food budget',
             '<p>The practical difficulty with cheese is how easily small pieces accumulate. One person offers a '
             'nibble during breakfast, another uses it for a tablet, and a third sprinkles it over dinner. Each '
             'person may think the amount is trivial while nobody has counted the combined intake. Keep one '
             'household record for food rewards rather than separate private allowances.</p><p><a '
             'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA sets a '
             'maximum of 10% of daily calories from all treats together</a>. Estimate daily energy with the <a '
             'href="/cat-calorie-calculator/">calorie calculator</a>, use the package’s energy information, and '
             'reserve room for every other treat. This is a calorie ceiling, not a validated safe cheese dose. A cat '
             'on a veterinary diet may need a different reward selected by the clinic even when a cheese piece fits '
             'the arithmetic.</p>'),
            ('Hiding a pill requires a medication check',
             '<p>Cheese is sometimes suggested as a convenient pill wrapper. Ask the prescribing clinic whether that '
             'specific medicine may be given with food and whether dairy is suitable. Do not assume that a technique '
             'suitable for one tablet applies to another, and do not crush or open medication unless instructed. A '
             'cat can also eat the wrapper and leave the tablet behind, so successful swallowing matters more than '
             'an empty treat bowl.</p><p>For a clinic-approved food reward, compare other options such as <a '
             'href="/can-cats-eat/chicken/">plain cooked chicken</a> with dairy choices like <a '
             'href="/can-cats-eat/yogurt/">yogurt</a>. Selection should follow the cat’s treatment and dietary '
             'restrictions. Avoid onion- or garlic-flavored cheese spreads: <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
             'links Allium ingredients to red blood cell damage, with cats particularly susceptible</a>. A flavored '
             'food cannot be made plain by scraping off the visible garnish.</p><p>If a clinic approves a particular '
             'cheese for a tablet, agree on one measured wrapper portion and who will give it. This prevents two '
             'family members from administering the same dose or each adding another unrecorded snack. Store the '
             'medication separately from the cheese package and record whether the tablet was swallowed, rather than '
             'merely whether food was offered.</p>'),
            ('After an accidental raid on the cheese plate',
             '<p>Put the remaining food away, identify what was actually eaten, and note whether wrappers or '
             'decorative picks are missing. A small plain nibble in a well cat and a large serving of an unknown '
             'spread need different discussions with a veterinarian. Do not label every episode of vomiting “lactose '
             'intolerance”; the timing alone cannot establish the cause.</p><p><a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell '
             'lists lethargy, weakness, reduced appetite, blood and accompanying diarrhea as reasons for prompt '
             'veterinary assessment of vomiting</a>. Supply the label or recipe and the approximate amount. If '
             'digestive upset follows dairy repeatedly, stop offering it rather than searching for a slightly '
             'different cheese that will permit the habit. Choosing a reward the cat tolerates, or using part of its '
             'regular food allowance, is simpler than managing a recurring food experiment.</p>')],
 'tuna': [('A tuna can and a complete tuna cat food have different jobs',
           '<p>The fish pictured on two containers can be the same while their nutritional roles are very different. '
           'Human canned tuna is a food ingredient. A feline diet that contains tuna may also include the vitamins, '
           'minerals and other nutrients needed for a complete ration. The decisive information is the '
           'nutritional-adequacy statement, not the fish name or how strongly your cat wants to eat it.</p><p><a '
           'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food">FDA '
           'explains that a complete-and-balanced claim identifies food intended as a sole diet, while treats and '
           'supplements generally do not serve that role</a>. Use the <a '
           'href="/guides/how-to-read-cat-food-labels/">cat-food label guide</a> to locate that statement. A cat '
           'that eats tuna enthusiastically is demonstrating preference, not confirming that a tuna-only menu will '
           'supply everything it needs. Do not replace a growing portion of complete food with plain fish simply '
           'because the bowl is emptied faster.</p><p>A pouch sold in the pet aisle can also be supplementary rather '
           'than complete. Do not assume that location in the shop settles the question. Keep a photograph of the '
           'adequacy statement alongside the product name when asking the clinic about a new food; that makes it '
           'easier to distinguish the intended staple from a topper with a similar label.</p>'),
          ('The packing liquid and recipe matter',
           '<p>Choose a plain product if the veterinary team allows tuna as a reward. Spring water is easier to '
           'assess than oil, brine, flavored sauce or a prepared tuna salad, but still read the label: “in water” '
           'does not necessarily mean that nothing else was added. Seasoned pouches and ready-made sandwich fillings '
           'deserve the same ingredient review as any human mixed dish.</p><p>Onion and garlic are particularly '
           'relevant to savory tuna preparations. <a '
           'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
           'identifies Allium ingredients as a cause of red blood cell injury in cats</a>. Taking visible onion '
           'pieces out of tuna salad does not remove the rest of the recipe. If an unsafe ingredient was eaten, use '
           'the <a href="/can-cats-eat/onions/">onion page</a> or <a href="/can-cats-eat/garlic/">garlic page</a> to '
           'prepare information for the veterinarian rather than treating the exposure as ordinary tuna.</p>'),
          ('Fish-only feeding is not a shortcut to better nutrition',
           '<p>Tuna is often promoted as a natural alternative for a finicky cat. The important distinction is '
           'between a limited reward and an unsupervised long-term diet. <a '
           'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
           'cautions that some cats eating canned fish products intended for humans have developed serious '
           'neurological problems</a>. This does not mean that one plain flake produces that outcome; it means that '
           'a human fish product should not be assumed to be a balanced feline staple.</p><p>Avoid adding '
           'supplements from several bottles to “fix” a tuna-only ration yourself. Feline diet formulation requires '
           'correct amounts and proportions, and an improvised addition may create a new imbalance. If your cat '
           'accepts nothing except tuna, arrange a veterinary appointment and bring a detailed diet history. The <a '
           'href="/guides/senior-cat-weight-and-appetite/">senior weight and appetite guide</a> is useful when this '
           'change accompanies weight loss or a newly selective appetite.</p>'),
          ('Use the aroma carefully, and keep track of the calories',
           '<p>A tiny amount of a clinic-approved tuna product may be useful as a reward, but repeatedly covering '
           'meals with it can make the day’s diet difficult to measure. Separate the reward portion before opening '
           'the cat’s regular food, record it, and ensure that every person in the home uses the same allowance. The '
           'liquid itself is not automatically calorie-free or appropriate for a medical diet.</p><p><a '
           'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA recommends '
           'limiting all treats to no more than 10% of daily energy</a>. The <a '
           'href="/cat-calorie-calculator/">calorie calculator</a> can estimate a starting daily target; your '
           'veterinarian may choose a different figure for the individual cat. Calculate from the actual product’s '
           'label rather than a generic spoonful. A numerical budget is an upper limit for extras, not a '
           'recommendation that tuna be eaten every day or that a particular serving is safe for every medical '
           'condition.</p>'),
          ('Cooked, raw and spoiled fish are separate questions',
           '<p>This page concerns plain canned tuna as an optional treat, not raw sushi fish or an aging open can. '
           '<a href="https://www.cdc.gov/healthy-pets/about/pet-food-safety.html">CDC advises safe handling of pet '
           'food and warns against raw animal foods because of harmful germs</a>. Keep opened food refrigerated as '
           'directed, use clean utensils, and do not use smell alone to establish that a forgotten portion is safe. '
           'See <a href="/can-cats-eat/raw-fish/">raw-fish risks</a> for why raw fish is not equivalent to the '
           'canned version.</p><p>If vomiting is repeated or accompanied by reduced appetite, weakness, lethargy, '
           'blood or diarrhea, seek veterinary advice using <a '
           'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell’s '
           'symptom guidance</a>. Bring the brand and ingredients, not just the word “tuna.” Persistent refusal of '
           'complete food deserves attention even when the cat is still willing to eat its favorite fish.</p>')],
 'chicken': [('Plain chicken has a useful but limited role',
              '<p>A small piece of cooked chicken can be a convenient reward because it is easy to separate into '
              'soft bits and its ingredients are easy to identify when cooked alone. That is different from '
              'declaring it the best food for every cat. The cat’s usual diet, treatment plan and tolerance still '
              'decide whether it is appropriate.</p><p><a '
              'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
              'describes cats as obligate carnivores while emphasizing their need for many nutrients beyond '
              'protein</a>. A piece of muscle meat supplies only part of that nutritional picture. It is not a '
              'complete ration because it came from an animal, and feeding larger amounts does not automatically '
              'improve the balance. Use chicken as a limited extra if the clinic agrees, while retaining a complete '
              'feline food as the main diet. For the difference between an ingredient and a complete product, '
              'consult the <a href="/guides/how-to-read-cat-food-labels/">cat-food label guide</a>.</p>'),
             ('Separate a portion before the family recipe begins',
              '<p>The easiest ingredient check is prevention: cook a small unseasoned portion apart from the main '
              'dish. Remove bones and skin, and let the meat cool before shredding or cutting it. Avoid taking '
              'chicken from a pot that has already received broth concentrate, onion, garlic, marinade or sauce. '
              'Visible white meat can still carry ingredients from the surrounding cooking liquid.</p><p><a '
              'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
              'identifies onions and garlic as causes of red blood cell damage in cats</a>. Rotisserie chicken is '
              'particularly difficult to judge without the full ingredient list, because seasoning can be applied '
              'before cooking. Picking off the skin does not prove that the remaining meat is unseasoned. Our <a '
              'href="/can-cats-eat/onions/">onion</a> and <a href="/can-cats-eat/garlic/">garlic</a> articles '
              'explain what information to provide after an exposure. A plain-looking supermarket slice and '
              'home-cooked plain chicken are not necessarily equivalent.</p><p>If several portions are being '
              'prepared for the week, label the plain cooked container before it goes into the refrigerator. Keep it '
              'separate from chicken already mixed with family sauces. This avoids a common practical mistake: '
              'remembering that some chicken was set aside, but later serving a piece from the wrong box because the '
              'meat looks the same.</p>'),
             ('Cooking is a real step, not a surface color',
              '<p>Use a food thermometer rather than judging poultry by whether its outside looks white. <a '
              'href="https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling">FDA’s safe-handling '
              'guidance specifies 165°F for poultry</a>. Let the cat’s portion cool and use clean utensils; keep raw '
              'cutting boards and juices away from cooked pieces. The same preparation habits protect the people who '
              'handle the food.</p><p>Raw chicken should not be substituted on the theory that it is more natural. '
              '<a href="https://www.cdc.gov/healthy-pets/about/pet-food-safety.html">CDC advises against raw pet '
              'food and raw animal treats because they can carry harmful germs</a>. A frozen or freeze-dried label '
              'does not, by itself, establish that every pathogen was eliminated. Leftovers need the storage and '
              'reheating practices appropriate to cooked food; do not offer a piece that has been sitting out '
              'through a long family meal simply because it is destined for a pet.</p>'),
             ('A chicken-and-rice bowl is not a long-term feline recipe',
              '<p>Chicken and rice are sometimes offered after digestive upset, but an improvised bland meal should '
              'not quietly become the permanent ration. <a '
              'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck '
              'describes nutritional deficiencies from limited homemade diets, including predominantly meat-based '
              'menus</a>. A veterinarian may prescribe a short-term plan or a properly formulated homemade diet, '
              'which is different from copying proportions from a social-media post.</p><p>If chicken is a reward, '
              'count it with all other extras under <a '
              'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA’s maximum '
              'of 10% of daily calories from treats</a>. The <a href="/cat-calorie-calculator/">calorie '
              'calculator</a> helps establish the scale of the day’s food, not a universal number of chicken cubes. '
              'Product and cooking method affect energy density, so use relevant food information when measuring. '
              'See <a href="/can-cats-eat/rice/">rice guidance</a> for why starch does not turn plain meat into a '
              'complete nutritional solution, and <a href="/can-cats-eat/turkey/">turkey</a> for a similar '
              'preparation question.</p>'),
             ('When a familiar reward is no longer suitable',
              '<p>A cat receiving a diet trial or a prescribed food may need every treat selected by the veterinary '
              'team. Do not assume that a single-ingredient chicken piece is automatically exempt from the plan. '
              'Write down rewards, toppers and foods used for medication so the clinic knows what the cat really '
              'receives; an incomplete diet history can make a response difficult to interpret.</p><p>If vomiting '
              'occurs with lethargy, weakness, reduced appetite, blood or diarrhea, follow <a '
              'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell’s '
              'advice to seek veterinary evaluation</a>. A cat that only wants chicken while abandoning complete '
              'food also needs attention rather than a steadily larger topping. Our <a '
              'href="/guides/senior-cat-weight-and-appetite/">senior weight and appetite guide</a> helps organize '
              'appetite and weight observations. The goal is to preserve a reliable daily diet and a useful reward, '
              'not let an attractive ingredient displace the nutritional foundation.</p>')],
 'cooked-eggs': [('A cooked egg is an optional food, not a coat supplement',
                  '<p>An egg can supply a small food reward without being necessary for a cat that already eats a '
                  'complete diet. Claims that eggs must be added for a shiny coat or stronger muscles overlook the '
                  'rest of the ration. <a '
                  'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
                  'explains that cats need many nutrients in proper amounts and usually do not need supplements '
                  'alongside balanced food</a>. A visually attractive ingredient does not identify what, if '
                  'anything, is missing from an individual cat’s diet.</p><p>Keep eggs in the role of a limited '
                  'extra when your veterinarian agrees they are suitable. Do not turn a daily egg into the '
                  'nutritional center of the bowl, and do not use an egg to repair a homemade diet without '
                  'professional formulation. The <a href="/guides/how-to-read-cat-food-labels/">cat-food label '
                  'guide</a> explains the more useful question: whether the regular food is complete for the cat’s '
                  'species and life stage.</p>'),
                 ('Fully set is the useful household preparation',
                  '<p>For simple sharing, boil an egg until its white and yolk are firm or scramble a small separate '
                  'amount without additions. <a '
                  'href="https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling">FDA advises firm '
                  'yolks and whites for eggs, with egg dishes cooked to 160°F</a>. Let the portion cool before '
                  'serving and cut or mash it into manageable pieces. Runny yolk and partly set white should not be '
                  'presented as equivalent to fully cooked egg.</p><p>Raw egg has additional concerns, explained on '
                  'our <a href="/can-cats-eat/raw-eggs/">raw-egg page</a>. <a '
                  'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck '
                  'describes avidin in raw egg white binding biotin and notes that cooking reduces antinutritional '
                  'factors</a>. This is a reason to distinguish preparations, not a claim that one raw lick '
                  'necessarily causes a deficiency. Heating also needs proper handling: keep raw shells and utensils '
                  'away from the cooked portion rather than treating cooking as the last possible contamination '
                  'point.</p>'),
                 ('The breakfast pan can change the ingredient list',
                  '<p>Scrambled eggs prepared for people often include milk, cream, cheese, butter, salt or '
                  'seasoning. A plain-looking curd may therefore be part of a mixed recipe. Make the cat’s portion '
                  'separately before additions, and avoid scraping a sample from a plate with sauces or garnishes. '
                  'An omelet containing onion cannot be made suitable by removing the visible onion pieces.</p><p><a '
                  'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
                  'identifies dairy as a cause of digestive upset in some pets and Allium ingredients as a cause of '
                  'red blood cell injury in cats</a>. Compare the <a href="/can-cats-eat/milk/">milk</a> and <a '
                  'href="/can-cats-eat/onions/">onion</a> pages for those separate issues. Egg mayonnaise, quiche, '
                  'breakfast sandwiches and flavored liquid-egg mixes require their own complete ingredient check. '
                  'The presence of cooked egg does not certify every food made with it.</p><p>Keep the reserved egg '
                  'portion clearly separate when preparing breakfast for several people. A spoon used to stir '
                  'seasoned eggs should not become the serving spoon for the plain portion. If somebody else feeds '
                  'the cat, tell them which container is suitable and how much has already been offered so that a '
                  'small extra does not become a second breakfast.</p>'),
                 ('A whole egg can be a large extra in a small animal’s day',
                  '<p>Do not copy a human serving size into a feline bowl. The relevant quantity is the energy in '
                  'the portion and its place alongside all other food rewards. CatCalc estimates resting energy as '
                  '70 × kilograms to the power 0.75, then applies the chosen life-stage or activity factor. The '
                  'resulting daily estimate is a starting point, not a prescription, and body condition and clinical '
                  'needs can change the target.</p><p><a '
                  'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA '
                  'recommends no more than 10% of total daily calories from treats</a>. Use the <a '
                  'href="/cat-calorie-calculator/">calorie calculator</a>, the actual preparation’s energy '
                  'information and a measured portion rather than a rule such as “one egg per cat.” The ceiling '
                  'includes every other treat as well. It does not establish a validated safe egg dose, and a '
                  'prescribed diet may require a different reward or none at all.</p>'),
                 ('When to stop the experiment and call the clinic',
                  '<p>Introduce no new food while trying to investigate ongoing vomiting or diarrhea without '
                  'veterinary guidance. If egg is followed by symptoms, write down the amount, recipe, timing and '
                  'other foods eaten, then stop offering it while seeking advice. A food diary is more useful than '
                  'repeatedly trying different egg preparations to see which one stays down.</p><p><a '
                  'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell '
                  'recommends prompt assessment for vomiting with weakness, lethargy, blood, reduced appetite or '
                  'accompanying diarrhea</a>. A cat that only wants egg while refusing complete food should also be '
                  'discussed with the veterinarian. The <a href="/guides/senior-cat-weight-and-appetite/">senior '
                  'weight and appetite guide</a> is useful for organizing appetite and weight observations. For a '
                  'suitable healthy cat, a small plain cooked taste can remain an occasional reward; it should not '
                  'distract from persistent symptoms, a medical feeding plan or a reliable complete daily '
                  'ration.</p>')],
 'cucumber': [('A garden cucumber and a pickle need separate answers',
               '<p>The <a '
               'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/cucumber">ASPCA '
               'entry for garden cucumber</a> classifies Cucumis sativus as non-toxic to cats. That narrow statement '
               'is useful, but it is not a verdict on every jar, salad or garnish made from cucumber. A plain piece '
               'from your cutting board has an ingredient list of one; a pickle may include brine, garlic, spices '
               'and other additions. Assess the product that is actually being offered.</p><p>If sharing is '
               'appropriate for your healthy cat, begin with washed fresh cucumber and prepare a small soft-looking '
               'piece you can supervise. Remove the ends and any skin that makes the piece harder for that cat to '
               'manage. Peeling is a practical preparation option, not evidence that all cucumber skin is poisonous. '
               'There is no reason to offer a whole cucumber as a chew object or leave a large round slice to be '
               'swallowed in a hurry.</p>'),
              ('Do not use food to stage a fright',
               '<p>A cucumber belongs on a food-preparation surface, not hidden behind a feeding cat to record a '
               'startled reaction. A meal is an opportunity for a predictable routine. Put any optional taste on a '
               "dish where the cat can approach or leave it voluntarily. Do not bring it close to the cat's face "
               'repeatedly or corner the animal after it backs away.</p><p>For a curious cat, a thin small piece or '
               'a little chopped flesh is easier to observe than a long slippery strip. Use a calm space away from '
               'dogs or competing cats. If it becomes a toy rather than something eaten, remove it after the '
               'interaction instead of losing track of food under furniture. These are simple supervision choices; '
               'they do not depend on claiming a special medical benefit for cucumber or interpreting a social-media '
               'reaction as a diagnosis.</p>'),
              ('What to inspect in brine, dressings and chilled soups',
               '<p>Pickled cucumber, tzatziki-style sauces, creamy salads and prepared soups should not inherit the '
               'plain-cucumber conclusion. Read the full label or recipe for <a '
               'href="/can-cats-eat/garlic/">garlic</a>, <a href="/can-cats-eat/onions/">onion</a> and dairy '
               'ingredients. <a '
               'href="https://www.aspca.org/news/pets-and-produce-top-tips-vegetable-garden-safety">ASPCA\'s garden '
               'guidance</a> discusses the specific Allium hazard in cats. A small quantity of cucumber does not '
               'neutralize an ingredient mixed through the dressing.</p><p>Do not rely on rinsing a finished pickle '
               'to prove it is suitable. You cannot tell from appearance how much of a seasoning remains, and there '
               'is an easier option: do not share it. Keep the jar or ingredient list if a cat has already licked a '
               'sauce. For the clinic, the useful description is the complete dish, approximate amount and time, '
               'rather than the reassuring front-of-pack vegetable name.</p>'),
              ('Water content does not make a treatment plan',
               '<p>It can be tempting to offer cucumber when a cat is drinking less or seems constipated. That '
               'changes the question from a snack decision to a health concern. Keep normal water sources available '
               'and discuss a sustained change in drinking or litter-box habits with the veterinarian. Cucumber '
               'should not be used to postpone that conversation. The <a '
               'href="/guides/senior-cat-weight-and-appetite/">senior appetite guide</a> gives context for recording '
               'changes rather than guessing their cause.</p><p><a '
               'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA\'s treat '
               'advice</a> also makes suitability for the individual cat important, especially with a medical '
               'condition or prescribed food. A general non-toxic classification cannot override that plan. If you '
               'just want an optional vegetable comparison, read <a href="/can-cats-eat/green-beans/">the green-bean '
               'notes</a>; neither food is a substitute for an agreed diet or an investigation of an unexplained '
               'symptom.</p>'),
              ('Count, observe and clear away',
               '<p>Use one small prepared portion rather than a continual supply from the chopping board. Count '
               'anything eaten with the other extras that day. Our <a href="/cat-calorie-calculator/">calorie '
               'calculator</a> estimates an overall energy starting point; it does not turn cucumber into a safe '
               'unlimited filler. If the cat refuses it, remove the dish and let its normal meal remain '
               'familiar.</p><p>Stop offering the snack after vomiting or loose stool, and contact the clinic if '
               'these recur, if the cat stops eating or if it appears painful. <a '
               'href="https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats">Merck\'s '
               'digestive-sign overview</a> shows why these changes need a history rather than an assumption that a '
               'watery vegetable must be soothing. Struggling to breathe or swallow needs urgent care. Tell the '
               'veterinarian whether peel, a large piece, packaging or a seasoned preparation could be involved. A '
               'concise record helps much more than testing another vegetable immediately.</p>')],
 'chives': [('A kitchen herb is still an Allium',
             '<p>Chives look very different from a bulb onion, but the relevant question is the plant family. <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/chives">ASPCA '
             'identifies chives, Allium schoenoprasum, as toxic to cats</a>. Its clinical summary includes red blood '
             'cell breakdown as well as digestive signs. The green blades should therefore not be offered as a fresh '
             'herb snack or mixed into cat food.</p><p>Do not confuse an indoor herb pot with cat grass simply '
             'because both present narrow green leaves. Keep the plant label when buying kitchen herbs and place '
             'chives where the cat cannot chew them. If an unidentified plant was nibbled, photograph the whole '
             'plant and the label rather than supplying a guess based on leaf shape. A reliable identification helps '
             'the veterinary team choose the relevant advice without treating every grass-like plant as the same '
             'exposure.</p>'),
            ('The garnish is part of the finished dish',
             '<p>Chives are often added after cooking, which makes them easy to overlook when someone describes a '
             'meal as plain. An omelet, soft cheese, potato topping or soup may contain chopped chives even if the '
             'main ingredient is otherwise familiar. Ask about garnish as well as seasoning when checking what a cat '
             'ate.</p><p>Our <a href="/can-cats-eat/cooked-eggs/">cooked-egg page</a> concerns eggs prepared without '
             'these extras. The <a href="/can-cats-eat/cheese/">cheese page</a> likewise does not give permission to '
             'share a flavored chive spread. For an accidental exposure, save the tub or recipe and estimate the '
             'amount of the whole dish eaten. Do not spend time sorting green flecks from a plate to calculate a '
             'supposedly safe count. Report the uncertainty and let a veterinarian assess the combination of '
             "ingredients and the cat's circumstances.</p>"),
            ('Why drying or cooking is not a clearance test',
             '<p><a '
             'href="https://www.merckvetmanual.com/toxicology/food-hazards/garlic-and-onion-allium-spp-toxicosis-in-animals">Merck\'s '
             'Allium review</a> includes chives in the same group as onions and garlic and explains that processed '
             'Allium foods can remain a concern. A dried herb jar belongs in the ingredient check; a cooked topping '
             'should not be assumed harmless because the green pieces have softened. There is no established '
             'household preparation that turns chives into a recommended feline treat.</p><p>This is different from '
             'the raw-versus-cooked decision for a food such as an egg. Cooking can address certain food-handling '
             'hazards, but it does not create a universal rule that every cooked ingredient is safe. When several '
             'risks share a plate, address all of them. For instance, identifying a plain cooked base does not clear '
             'a dish after chives have been stirred through it. Set aside any suitable cat portion before adding the '
             'herb.</p>'),
            ('Signs are not limited to an upset stomach',
             '<p>The <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/chives">ASPCA '
             'chive entry</a> lists weakness, blood in urine, a high heart rate and panting among possible signs, '
             'along with vomiting and hemolytic anemia. Seek prompt veterinary help for concerning changes after an '
             'exposure, and use emergency care for collapse or trouble breathing. A symptom list is a reason to get '
             'help, not a home method for confirming the cause.</p><p>Give the clinic the time chives were available '
             'and the time any change was first seen. Include other Allium exposure, such as <a '
             'href="/can-cats-eat/onions/">onion</a> in the same soup or <a href="/can-cats-eat/garlic/">garlic</a> '
             'in the spread. If the cat has been grazing on an herb pot for an unknown period, say so. The history '
             'should distinguish a witnessed single bite from repeated access rather than forcing both situations '
             'into an exact amount.</p>'),
            ('Manage herb pots and meal preparation together',
             '<p>A shelf of cooking herbs and a plate of leftovers are two separate access points. Move a chive pot '
             'into a closed room or another place the cat cannot enter; do not rely only on moving it a little '
             'higher. During meal preparation, collect trimmings directly into a closed container instead of leaving '
             'a small pile on the counter.</p><p>Before serving guests, explain that green garnish counts when '
             "deciding whether food can be shared. Provide a bowl with the cat's usual food if someone wants to give "
             'a reward. After eating, clear chive-smeared plates and utensils before the cat investigates them. Our '
             '<a href="/guides/how-catcalc-rates-human-foods/">food-rating guide</a> explains why ingredient '
             'identification comes before calories. A garnish may contribute little energy to a human meal while '
             'still being an ingredient that should not be intentionally offered to a cat.</p>')],
 'alcohol': [('A spill is an exposure, even when nobody offered a drink',
              '<p>Alcohol accidents are not limited to someone deliberately giving a cat beer. An unattended glass, '
              'a tipped cocktail or a liquor-filled sweet can create access. <a '
              'href="https://www.petpoisonhelpline.com/poison/alcohol/">Pet Poison Helpline</a> identifies alcoholic '
              'drinks, liquor-containing candies and unbaked yeast dough as potential sources of ethanol exposure. '
              'Record what the cat actually reached rather than describing the event only as a kitchen '
              'accident.</p><p>For a beverage, keep the bottle or a photograph showing its name and alcohol '
              'concentration. For a cocktail, list the spirits, mixer and any extra flavorings. If the amount is '
              'unknown because a glass spilled, estimate how much was present before and after without claiming that '
              'everything missing was swallowed. Say clearly whether the cat was seen drinking, was found beside the '
              'spill, or had liquid on its coat. Those are different observations for the veterinary team.</p>'),
             ('Alcohol affects more than coordination',
              '<p>The <a '
              'href="https://www.msdvetmanual.com/toxicology/toxicoses-from-household-hazards/toxicoses-from-alcohols-in-animals">MSD '
              'Veterinary Manual alcohol review</a> describes rapid absorption and effects including nervous-system '
              'depression, reduced body temperature and metabolic disturbance. A cat staggering after an exposure '
              'should not be treated as an amusing version of human drunkenness. Severe intoxication can impair '
              'breathing and become life-threatening.</p><p>Seek veterinary help promptly for suspected ingestion, '
              'and emergency care if there is difficulty breathing, collapse, seizures or marked inability to '
              'respond normally. Vomiting and poor coordination also deserve immediate reporting. Do not wait for '
              'every symptom on a list to appear. A list describes possible effects, not a checklist that must be '
              'completed before the situation counts as serious. Record the time each observed sign started so the '
              'clinic can relate changes to the possible exposure and decide what care is needed.</p>'),
             ('Mixed drinks need a complete ingredient description',
              '<p>A coffee cocktail is both an alcohol question and a <a href="/can-cats-eat/coffee/">caffeine '
              'question</a>. A chocolate liqueur also belongs in the <a href="/can-cats-eat/chocolate/">chocolate '
              'discussion</a>. These ingredients should be mentioned together when asking for advice, rather than '
              'making separate assumptions that each amount seems too small to matter. Keep a recipe or bar receipt '
              'if it helps identify what was served.</p><p>Human calorie labels and sugar-free claims do not answer '
              'the alcohol question. Likewise, a creamy texture does not make a drink equivalent to the <a '
              'href="/can-cats-eat/milk/">milk discussed on its own page</a>. For cooking sauces or desserts, '
              'describe the recipe and preparation as accurately as possible instead of deciding from taste that all '
              'alcohol must be gone. When the amount remaining is uncertain, tell the clinician that; an unsupported '
              'estimate should not become the basis for home reassurance.</p>'),
             ('Not every product called alcohol is a beverage',
              '<p><a '
              'href="https://www.msdvetmanual.com/toxicology/toxicoses-from-household-hazards/toxicoses-from-alcohols-in-animals">MSD</a> '
              'distinguishes ethanol from other alcohols found in household products, including methanol and '
              'isopropanol. The product name therefore matters. A cat licking a cleaning liquid should not be '
              'described as simply having had a sip of alcohol; bring the container so its ingredients can be '
              'identified. Tell the clinic about skin or coat contact as well as anything swallowed.</p><p>This page '
              'is not a cleaning-product treatment guide. Do not apply another household chemical, give a home '
              'antidote or improvise care from a human first-aid recipe. Ask the veterinary team how to manage the '
              'actual exposure while arranging care. Keeping the original container upright and away from the cat '
              'also prevents another exposure during the call. If there are other pets, check where they are before '
              'beginning cleanup so the spill is not left accessible to them.</p>'),
             ('A safer routine for entertaining and home brewing',
              '<p>Before guests arrive, decide where drinks will be placed and who clears them. Use a room the cat '
              'cannot enter for unattended serving trays, open punch bowls or brewing equipment. Collect '
              'half-finished glasses before going to bed instead of assuming the room is safe once people leave. '
              'Wipe spills promptly and keep the cat away while cleanup is in progress.</p><p>Remember that <a '
              'href="/can-cats-eat/raw-dough/">raw yeast dough</a> can generate ethanol after ingestion, even when '
              'no beverage is involved. Proof dough and discard brewing or baking waste in inaccessible containers. '
              "Ask visitors to give only the cat's usual food if they want to offer a reward. A consistent no-drinks "
              'rule is easier to follow than making exceptions for a particular beer, a small glass or a cat that '
              'has appeared unaffected in the past.</p>')],
 'coffee': [('Identify the caffeine source before estimating the amount',
             '<p>The word coffee can mean a weak finished drink, an espresso concentrate, dry grounds or whole '
             'beans. <a href="https://www.petpoisonhelpline.com/poison/caffeine/">Pet Poison Helpline</a> explains '
             'that concentrated sources such as grounds, tea bags and supplements can present a more serious '
             'poisoning concern than a small lick of a beverage. Do not infer the amount of caffeine from the size '
             'or color of the spill alone.</p><p>When calling a veterinarian, name the brand and the exact product. '
             'Keep the container, serving information and any caffeine figure printed on it. If the drink came from '
             'a cafe, note the size and number of added shots if known. For an open packet of grounds, estimate the '
             'amount missing and explain whether the cat may have scattered some. A realistic range is better than '
             'claiming every missing gram was swallowed or dismissing it all as spilled material.</p>'),
            ('Milk and sweetness do not cancel the stimulant',
             '<p><a '
             'href="https://www.vet.cornell.edu/hospitals/pharmacy/consumer-clinical-care-guidelines-animals/small-animal-toxins">Cornell\'s '
             'small-animal toxin reference</a> identifies caffeine as toxic to cats and dogs. A milk-heavy coffee '
             'remains a caffeine-containing mixture. Cream, syrup or an iced presentation changes the product '
             'description; none is a way to make a coffee drink suitable for a cat. For the separate digestive '
             'limitations of dairy, see our <a href="/can-cats-eat/milk/">milk guide</a>.</p><p>A mocha can also '
             'contain <a href="/can-cats-eat/chocolate/">chocolate</a>, and a coffee cocktail brings in <a '
             'href="/can-cats-eat/alcohol/">alcohol</a>. Mention those ingredients during the same consultation. Do '
             'not focus on whichever ingredient sounds most familiar and leave out the others. If a sugar-free syrup '
             'was added, photograph its ingredient list. Cats do not necessarily share the dog response to every '
             'sweetener, so accurate identification is more useful than treating the phrase sugar-free as a complete '
             'toxicology answer.</p>'),
            ('Notice changes in activity without trying to diagnose them',
             '<p>According to <a href="https://www.petpoisonhelpline.com/poison/caffeine/">Pet Poison Helpline</a>, '
             'caffeine poisoning can involve unusual hyperactivity, digestive upset, changes in heart rate or '
             'rhythm, tremors and seizures. A restless cat is not simply getting a harmless energy boost. Report '
             'pacing, agitation, vomiting or shaking after a possible exposure and seek emergency care for seizures, '
             "collapse or trouble breathing.</p><p>Do not try to judge heart safety from a cat's apparent "
             'willingness to play. Some important changes need clinical assessment, and an owner watching at home '
             'cannot rule them out. If a veterinarian recommends observation, ask exactly which changes should '
             'trigger another call and where to obtain help overnight. Keep the original time of access in your '
             'notes; discovering a symptom later does not mean the cat must have found a second source of '
             'coffee.</p>'),
            ('The bin can matter as much as the mug',
             '<p>A morning coffee routine can leave grounds, filters, pods and stirrers in several places. Collect '
             'them directly into a closed waste container instead of leaving an open filter basket or used espresso '
             'puck on the counter. If a pod or bag is torn, tell the clinic whether pieces of its packaging are '
             'missing as well as its contents. Keep food-exposure details separate from possible swallowed '
             'objects.</p><p>Check backpacks and desk drawers for energy supplements or tablets. <a '
             'href="https://www.petpoisonhelpline.com/poison/caffeine/">The poison-center caffeine resource</a> '
             'lists concentrated energy products among the sources encountered in pets. Store them with the same '
             'care as other products the cat must not access. Decaffeinated labeling is not an invitation to offer '
             'the drink; there is no feline nutritional reason to make coffee part of the feeding routine, and the '
             'complete ingredient mix still requires attention after an accident.</p>'),
            ('Choose a different ritual for sharing breakfast',
             '<p>If your cat joins you at breakfast, place a portion of its usual food or another suitable reward in '
             'its own dish before opening the coffee supplies. This preserves a shared routine without letting the '
             'cat lick the mug, spoon or spilled drink. Teach everyone in the house the same rule, including guests '
             'who may think a creamy coffee is mostly milk.</p><p>The <a href="/cat-calorie-calculator/">calorie '
             'calculator</a> is useful for budgeting ordinary food and treats, but it cannot evaluate caffeine. Low '
             'sugar, few calories or a small serving size does not resolve a poisoning question. Our <a '
             'href="/guides/how-catcalc-rates-human-foods/">food-rating method</a> separates toxic ingredients from '
             'routine feeding limits. After suspected caffeine ingestion, seek advice based on the product, amount '
             'and individual cat, rather than trying to fit the drink into a daily energy allowance or borrowing a '
             'human caffeine limit.</p>')],
 'raw-dough': [('Two hazards can develop from the same mouthful',
                '<p>Raw yeast dough creates a problem that is different from an ordinary bread crumb. The <a '
                'href="https://www.merckvetmanual.com/toxicology/food-hazards/bread-dough-toxicosis-in-animals">Merck '
                'Veterinary Manual dough review</a> explains that yeast can continue fermenting in the stomach, '
                'causing expansion and producing ethanol. Stomach distension and alcohol intoxication are therefore '
                'related consequences of one exposure, not two unrelated accidents that an owner has to recognize '
                'separately.</p><p>This applies to yeast-based bread and pizza dough before it is fully baked. Tell '
                'the veterinarian what stage the dough had reached and whether it contained fillings or toppings. If '
                'it was made from a mix, keep the package; if homemade, save the recipe. A description such as flour '
                'and water leaves out the yeast and other ingredients that make the clinical question different from '
                'a lick of loose flour.</p><p>Also report whether dough was eaten alone or together with a towel, '
                'bag or other covering.</p>'),
               ('Proofing is an access problem, even under a cloth',
                '<p>A bowl covered with a towel may keep dust off the dough, but it is not a reliable cat barrier. '
                'Put proofing dough in a place the cat cannot enter or open, and check that any chosen container is '
                'appropriate for the baking process. Clean scraps from the worktop and floor as soon as shaping is '
                'finished.</p><p>The <a href="https://www.aspcapro.org/resource/bread-ingestion-pets">ASPCApro '
                'bread-ingestion guidance</a> specifically warns that pets should not reach dough left to rise. '
                'Include bread-machine pans, discarded crust trimmings and pizza-preparation bowls in the cleanup '
                'routine. If dough is missing, distinguish a witnessed bite from an estimate based on a torn '
                'covering. Do not assume that dough left in a warm location has become safe just because it has '
                'risen. Fully baked bread is a different product, discussed on our <a '
                'href="/can-cats-eat/bread/">bread page</a>.</p>'),
               ('Know the difference between a recipe category and a clearance',
                '<p>Not all uncooked mixtures contain yeast. A biscuit dough, cake batter and yeasted pizza base are '
                'different recipes, so tell the clinic which one was involved. The particular expansion-and-ethanol '
                'mechanism described here concerns yeast-based dough; this distinction does not establish that every '
                'other raw mixture is safe to feed.</p><p>Other ingredients create separate questions. '
                'Egg-containing batter belongs in the <a href="/can-cats-eat/raw-eggs/">raw-egg discussion</a>, and '
                'cocoa or chocolate chips bring the <a href="/can-cats-eat/chocolate/">chocolate concern</a>. Garlic '
                'in a dough or topping needs to be reported too. Keep the full recipe together instead of calling '
                'about each ingredient independently. If the recipe is unknown, say that and retain a photograph or '
                'product name. The goal is accurate identification, not forcing an unfamiliar food into a reassuring '
                'category.</p>'),
               ('An enlarged abdomen or drunken behavior requires urgent care',
                '<p><a '
                'href="https://www.merckvetmanual.com/toxicology/food-hazards/bread-dough-toxicosis-in-animals">Merck</a> '
                'describes abdominal distension, unsuccessful retching and lethargy among possible early changes, '
                'with poor coordination and more serious nervous-system effects as ethanol intoxication develops. '
                'Contact a veterinarian promptly after a suspected ingestion rather than waiting to see whether the '
                'dough rises visibly inside the cat. Breathing difficulty, collapse, seizures or profound weakness '
                'requires emergency attention.</p><p>Our <a href="/can-cats-eat/alcohol/">alcohol guide</a> explains '
                'the ethanol side of the concern. Do not try to treat a cat as if it merely needs to sleep after a '
                'drink. Likewise, do not use kitchen remedies intended to stop fermentation or move the dough along. '
                'Follow direct veterinary instructions for the actual exposure. A treatment described in a '
                'professional reference is not automatically an appropriate procedure for an owner to perform at '
                'home.</p>'),
               ('Make the next baking session easier to supervise',
                '<p>Before opening ingredients, choose where the cat will stay during mixing, proofing and cleanup. '
                'Put finished bread in a separate place so raw dough and baked food cannot be confused. Close the '
                'waste bin after discarding scraps and check utensils before placing them in a sink accessible to '
                'the cat. A predictable routine is easier to maintain than chasing the animal away from each new '
                'bowl.</p><p>If a guest or child helps bake, explain that an unbaked piece is not a treat for the '
                "cat. Provide the cat's own food if someone wants to reward it for staying in another room. Neither "
                'a tiny calorie count nor an otherwise plain recipe creates a safe allowance for yeast dough. The <a '
                'href="/guides/how-catcalc-rates-human-foods/">food-rating guide</a> places this in an urgent hazard '
                'category because food preparation and the fermentation process matter more than the name '
                'bread.</p>')],
 'yogurt': [('A live-culture label is not a treatment plan',
             '<p>A yogurt pot can advertise live cultures without demonstrating that the product will treat a cat’s '
             'digestive disease. The name of an ingredient is not evidence for a clinical benefit in a particular '
             'species, at a particular dose, for a particular condition. If a veterinarian recommends a probiotic, '
             'ask which product and how to judge the response rather than substituting a human breakfast '
             'food.</p><p>Yogurt remains a dairy food. <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
             'warns that milk and other dairy products can cause digestive upset when lactose is poorly '
             'digested</a>. Fermentation does not justify assuming that every yogurt contains no lactose or that '
             'every cat can tolerate it. A cat with ongoing diarrhea needs an assessment of the problem; adding more '
             'yogurt can make it harder to know which dietary change was responsible for the next symptom.</p>'),
            ('Plain means checking the whole container',
             '<p>Look past the fruit pictured on the lid. Fruit preparations, flavored syrups, chocolate pieces, '
             'granola and sweeteners turn a pot into a mixture, and some ingredients may be packaged in a separate '
             'compartment. Do not assume that a spoonful taken from the white part has an ingredient list different '
             'from the combined product. If you cannot identify the ingredients, choose a reward already approved '
             'for the cat instead.</p><p>Read <a href="/can-cats-eat/chocolate/">chocolate guidance</a> for '
             'cocoa-containing products and <a href="/can-cats-eat/xylitol/">xylitol guidance</a> for the important '
             'distinction between feline and canine evidence. <a '
             'href="https://www.aspcapro.org/resource/most-common-sleep-aid-toxicities-cats-and-dogs">ASPCApro '
             'describes gastrointestinal upset from xylitol in cats</a>; the well-known dog poisoning pattern should '
             'not be automatically asserted for cats. An unknown sugar-free mixture still warrants a call with the '
             'actual label, especially if other hazardous ingredients are involved.</p><p>Keep the lid and the outer '
             'sleeve until you know which product was eaten; the reusable pot alone may not carry the complete '
             'ingredient list. If multiple pots are open in a shared fridge, label the one intended for a '
             'clinic-approved food task. This avoids confusing a plain product with an almost identical flavored or '
             'sweetened version.</p>'),
            ('Greek, lactose-free and plant-based are different claims',
             '<p>“Greek” describes a style of yogurt, not proof of suitability for a cat. “Lactose-free” addresses '
             'one sugar, not whether a product is complete feline nutrition. A plant-based yogurt is not dairy, but '
             'it may contain its own flavorings and sweeteners; the absence of cow’s milk does not certify the rest '
             'of the recipe. None of these labels creates a reason to supplement a complete cat diet.</p><p><a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
             'explains that cats require a carefully balanced supply of nutrients and generally do not need '
             'supplements alongside a complete diet</a>. Compare the role of yogurt with <a '
             'href="/can-cats-eat/milk/">milk</a> and <a href="/can-cats-eat/cheese/">cheese</a> rather than '
             'arranging dairy foods into a universal safe-to-unsafe ladder. An individual history of poor tolerance '
             'is more useful than a marketing category.</p>'),
            ('How an optional taste fits into a real day',
             '<p>If your veterinary team agrees that a particular plain product is suitable, treat any taste as part '
             'of the food budget. Do not begin with a standard teaspoon for every cat: spoon sizes, product energy '
             'density, medical needs and tolerance vary. An amount that contributes few calories can still cause '
             'trouble for a sensitive cat, so a calorie calculation cannot be used as a tolerance test.</p><p><a '
             'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA recommends '
             'no more than 10% of daily calories from treats</a>. Add yogurt to the same tally as biscuits and '
             'training rewards, using the <a href="/cat-calorie-calculator/">calorie calculator</a> only as a '
             'starting estimate for the daily total. Our <a href="/guides/how-to-read-cat-food-labels/">cat-food '
             'label guide</a> explains the difference between supplementary foods and complete diets. If the cat '
             'refuses its normal meal but eagerly eats yogurt, contact the clinic about appetite rather than letting '
             'yogurt become the replacement meal.</p>'),
            ('What to record if the next litter-box visit is abnormal',
             '<p>Stop the new food and write down the product, approximate amount, time and other recent changes. '
             'Keep the container for its ingredient list. Avoid offering several different dairy products in '
             'succession; that creates a confusing food history rather than a controlled answer to whether yogurt '
             'was tolerated.</p><p>Repeated vomiting, blood, weakness, lethargy or a reduction in appetite should '
             'prompt veterinary advice, as described in <a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell’s '
             'vomiting guidance</a>. Be especially clear if a prescribed diet or treatment was already in progress. '
             'Yogurt cannot diagnose food intolerance, replace fluid treatment, or establish that the intestine has '
             'recovered. For an older cat with appetite or weight changes, the <a '
             'href="/guides/senior-cat-weight-and-appetite/">senior weight and appetite guide</a> can help organize '
             'observations for the appointment without turning a yogurt preference into a diagnosis.</p>')],
 'raw-fish': [('Two risks that should not be collapsed into one',
               '<p>Raw fish raises both food-safety and nutritional questions. Germs can be present in uncooked '
               'animal foods, while particular fish can also contain enzymes that interfere with nutrients. These '
               'are different mechanisms: a product might look fresh and still carry a food-safety risk, and '
               'repeated use of an unsuitable raw fish diet can create a nutritional problem without an obvious '
               'spoiled smell.</p><p><a '
               'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
               'does not recommend raw diets because they can carry bacteria, viruses and parasites without a '
               'demonstrated clear health advantage</a>. This concern extends to people who handle the food or touch '
               'contaminated bowls and surfaces. Keeping a raw-fish portion separate from human dinner does not '
               'remove the exposure pathway. Choose a cooked, boneless preparation instead of treating a pet-food '
               'label or a sushi counter as proof that raw fish is appropriate for cats.</p>'),
              ('What thiaminase actually means',
               '<p>Thiamine is vitamin B1. Thiaminases are enzymes in some raw fish that break it down, which can '
               'matter when those foods are fed repeatedly as a substantial part of the diet. <a '
               'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck '
               'Veterinary Manual describes thiaminases in raw freshwater fish and clams, their destruction by '
               'cooking, and neurological signs of thiamine deficiency in cats</a>. The mechanism is not a claim '
               'that all fish species contain equal amounts or that one lick inevitably causes deficiency.</p><p>It '
               'also does not justify adding an arbitrary vitamin tablet to raw fish. A supplement selected at home '
               'cannot certify that the whole diet is complete or address microbial hazards. If raw fish has become '
               'a regular meal, tell your veterinarian the species, amount, frequency and duration. Include any '
               'supplements already used so that the diet can be assessed as a whole.</p><p>A useful history '
               'includes whether the fish was a small reward, a topper or the main meal. “Sometimes” and “a little” '
               'can mean very different things in different homes. Estimate the number of meals per week and the '
               'duration of the habit, and name the fish when possible. Those concrete details help the clinic '
               'assess dietary exposure without guessing.</p>'),
              ('Freezing and marinating do not create a complete safety plan',
               '<p>A household freezer is a storage tool; it should not be treated as evidence that every possible '
               'pathogen has been eliminated. Likewise, citrus marinade, salting, drying or the words “human grade” '
               'do not convert a raw animal product into a complete feline ration. Different processes address '
               'different hazards, and you should not infer a universal kill step from a kitchen technique.</p><p><a '
               'href="https://www.cdc.gov/healthy-pets/about/pet-food-safety.html">CDC recommends against raw pet '
               'food and treats because of germs such as Salmonella and Listeria</a>. Wash hands, utensils and '
               'food-contact surfaces after handling raw fish, and keep the cat away during preparation. Do not '
               'offer trimmings while waiting for the main portion to cook. A cooked fish reward is a separate '
               'decision, explained on the <a href="/can-cats-eat/salmon/">cooked-salmon page</a> and <a '
               'href="/can-cats-eat/tuna/">tuna page</a>.</p>'),
              ('How cooking changes the decision',
               '<p>Cook plain fish before adding human sauces, then inspect it carefully for bones and let the cat’s '
               'small portion cool. <a '
               'href="https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling">FDA’s food-handling '
               'guidance gives 145°F for fin fish, or opaque flesh that separates easily with a fork</a>. These are '
               'household food-safety instructions, not a veterinary prescription or a guarantee that every prepared '
               'dish is suitable. Garlic butter, onion sauce and salty marinades remain separate problems after '
               'cooking.</p><p>Cooked fish still needs a dietary role. <a '
               'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA advises '
               'that all treats together contribute no more than 10% of a cat’s daily calories</a>. Use the <a '
               'href="/cat-calorie-calculator/">calorie calculator</a> to understand the day’s total, and use '
               'complete cat food for the main ration. Cooking destroys thiaminase but does not, by itself, add all '
               'the nutrients missing from a fish-only homemade menu.</p>'),
              ('What to tell the clinic after exposure',
               '<p>For a stolen raw-fish piece, record the time, approximate amount, fish type if known, seasoning '
               'and whether bones were present. For habitual feeding, describe the full menu rather than only the '
               'most recent bite. These details help the veterinarian decide which exposure or nutritional issues '
               'need attention. Do not induce vomiting or start a vitamin treatment from an internet dose '
               'chart.</p><p>Loss of coordination, seizures or marked weakness need urgent veterinary assessment; '
               'Merck includes neurological dysfunction among feline thiamine-deficiency signs. Repeated vomiting, '
               'reduced appetite, lethargy or accompanying diarrhea also warrant advice, as outlined by <a '
               'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell</a>. '
               'Symptoms cannot establish thiamine deficiency at home, and the absence of symptoms does not validate '
               'continuing the same raw diet. The <a href="/guides/how-to-read-cat-food-labels/">cat-food label '
               'guide</a> can help prepare a more suitable long-term feeding discussion.</p>')],
 'raw-eggs': [('The shell does not certify a sterile breakfast',
               '<p>An intact-looking egg is still an uncooked animal food. Cracking it into a clean bowl does not '
               'establish that harmful bacteria are absent. <a '
               'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
               'warns that raw eggs can contain Salmonella or E. coli that can harm pets and people</a>. A cat does '
               'not need to appear ill immediately for the household’s handling practices to matter; raw residues on '
               'utensils and surfaces are another exposure route.</p><p>Do not let the cat lick the bowl used for '
               'cake batter or mayonnaise. Those mixtures can introduce other ingredients in addition to raw egg. '
               'Keep preparation bowls away from pets, clean the counter and wash hands after handling eggs. The '
               'appropriate alternative, when an egg reward fits the cat’s diet, is a separately cooked plain '
               'portion described on our <a href="/can-cats-eat/cooked-eggs/">cooked-egg page</a>.</p><p>Do not '
               'leave a cracked egg or batter bowl unattended while preheating the oven. Put shells straight into a '
               'covered waste container and keep the cat off the preparation surface. If another person finishes the '
               'recipe, explain which utensils contacted raw egg so that cleaning does not depend on remembering '
               'where a bowl happened to stand.</p>'),
              ('Avidin binds a vitamin; it is not instant poisoning',
               '<p>Raw egg white contains avidin, a protein that binds biotin and can interfere with its absorption. '
               '<a '
               'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck '
               'Veterinary Manual explains this interaction and the role of cooking in reducing antinutritional '
               'factors</a>. The concern is especially relevant to repeated feeding in an unbalanced diet. It should '
               'not be exaggerated into a claim that one small lick immediately strips vitamins from the cat’s '
               'body.</p><p>Egg yolk contains nutrients, but feeding yolks while discarding whites is not a complete '
               'nutritional solution. It does not create a balanced feline menu, and a raw yolk remains a raw '
               'animal-food exposure. Likewise, a biotin supplement does not resolve the microbial question. If '
               'someone has been routinely adding raw eggs to the bowl, bring the whole diet history to the '
               'veterinarian instead of trying to repair a single nutrient in isolation.</p>'),
              ('Soft yolks, pasteurized products and cooking',
               '<p>For simple home sharing, fully cooked egg is easier to assess than an uncooked mixture. <a '
               'href="https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling">FDA advises cooking '
               'eggs until both white and yolk are firm, with egg dishes reaching 160°F</a>. Cool the portion and '
               'keep it plain. Runny breakfast eggs, a raw egg cracked onto kibble and a fully set boiled egg are '
               'different preparations even though all began in the same carton.</p><p>Pasteurization is a '
               'processing claim, not proof that an egg product is a complete diet or suitable in unlimited '
               'quantities. Check the package and follow its directions; do not infer that all liquid egg products '
               'have identical ingredients. Milk, cheese, cooking fat, onion and seasoning can be added before or '
               'after heating. Our <a href="/can-cats-eat/milk/">milk</a> and <a '
               'href="/can-cats-eat/onions/">onion</a> pages explain why those additions require their own '
               'assessment.</p>'),
              ('Why an egg is an extra rather than a nutritional fix',
               '<p>A raw egg is sometimes proposed for a shinier coat or to compensate for a low-quality diet. That '
               'substitutes a kitchen habit for checking whether the main food is nutritionally adequate. <a '
               'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food">FDA '
               'distinguishes complete-and-balanced foods from treats and supplements</a>; the right question is '
               'whether the staple meets the cat’s life-stage needs, not whether another ingredient sounds '
               'nutritious.</p><p>If cooked egg is allowed as a reward, count it with the day’s other extras. <a '
               'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA limits '
               'treats to no more than 10% of daily calories</a>. Use the <a href="/cat-calorie-calculator/">calorie '
               'calculator</a> as a starting estimate and the actual egg preparation’s energy information where '
               'available. Do not copy a whole-egg serving from a human breakfast plan. An energy allowance is not a '
               'validated safe egg dose or permission to bypass a medical diet.</p>'),
              ('A useful response to a stolen lick',
               '<p>Remove the raw mixture and identify everything it contained. Plain egg white, chocolate cake '
               'batter and a bowl of seasoned ground meat call for different advice. Keep the ingredient labels and '
               'note the time and approximate amount. Contact your veterinarian if a potentially toxic co-ingredient '
               'was involved; do not wait for the raw-egg question to be settled first.</p><p>For illness after any '
               'exposure, <a '
               'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell '
               'recommends prompt evaluation when vomiting accompanies weakness, lethargy, reduced appetite, blood '
               'or diarrhea</a>. A veterinarian can decide what monitoring or testing is appropriate for the '
               'individual cat. Do not give antibiotics, vitamin doses or human stomach remedies as a precaution. '
               'The <a href="/guides/how-to-read-cat-food-labels/">cat-food label guide</a> offers a better route '
               'for long-term nutrition: verify the regular diet and discuss changes with the clinic rather than '
               'adding raw ingredients to it.</p>')],
 'bones': [('The meat and the bone are separate feeding decisions',
            '<p>A cat may be able to have a small amount of plain cooked poultry while the bone from the same meal '
            'remains unsuitable. <a '
            'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA\'s '
            'cat-treat guidance</a> warns that both cooked and raw bones can cause significant damage when chewed or '
            'swallowed. The question is mechanical injury as well as food safety; the familiar origin of a bone does '
            'not remove that concern.</p><p>Our <a href="/can-cats-eat/chicken/">chicken guide</a> and <a '
            'href="/can-cats-eat/turkey/">turkey guide</a> describe boneless meat. Set aside the intended portion '
            'before serving the human meal, inspect it carefully and keep carcasses inaccessible. Do not hand over a '
            'partly cleaned bone so the cat can strip the remaining meat. A safe-looking piece of meat attached to '
            'an unsafe object is still a different feeding choice from a separately prepared, boneless treat.</p>'),
           ('Cooking and size do not provide a reliable safety rule',
            '<p><a href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA\'s '
            'feline treat guidance</a> warns that both cooked and raw bones can cause significant damage when chewed '
            'or swallowed. The <a '
            'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/potentially-dangerous-items-your-pet">FDA</a> '
            'explains that bones can become stuck in the esophagus, stomach or intestines. Raw bones are not a '
            'guaranteed alternative. There is no household rule that a bone is safe merely because it is large, '
            "soft-looking or has been chewed successfully before.</p><p>Avoid using the cat's enthusiasm as a test "
            'of suitability. A cat accepting an object says nothing about what happens after swallowing it. If a '
            'bone has already been eaten, keep any similar remaining piece or take a photograph with a size '
            'reference. Tell the clinic whether the bone was roasted, boiled, fried or raw, and whether it was '
            'swallowed whole or broken. These details describe the event without claiming that a particular '
            'preparation makes it harmless.</p>'),
           ('Describe swallowed objects as well as the meal',
            '<p>The <a '
            'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/potentially-dangerous-items-your-pet">FDA\'s '
            'pet-hazard guidance</a> identifies bones as objects that can obstruct the esophagus, stomach or '
            'intestines. A cat eating leftovers may also encounter foil, skewers or other packaging, so report '
            'anything else that is missing. Do not focus entirely on a food ingredient while overlooking a possible '
            'foreign object.</p><p>Retain the plate, carcass or container long enough to establish what could have '
            'been reached. Separate a witnessed swallowed piece from a merely missing one. If several pets were '
            'present, explain that the identity of the animal involved may be uncertain. A clear photograph and a '
            'practical estimate are more useful than trying to reconstruct a perfect bone count while delaying the '
            'call. Ask the veterinarian what should be brought to the clinic and whether any particular observations '
            'are needed during transport.</p>'),
           ('Do not wait for a digestive emergency to become obvious',
            '<p>Choking, trouble breathing or collapse requires emergency care. Difficulty swallowing, repeated '
            'gagging, drooling, vomiting or apparent pain after a bone exposure also warrants prompt veterinary '
            'contact. <a '
            'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/potentially-dangerous-items-your-pet">FDA '
            'guidance</a> emphasizes the obstruction risk from swallowed bones, while <a '
            'href="https://www.merckvetmanual.com/digestive-system/surgical-problems-of-the-gastrointestinal-tract-in-small-animals/gastrointestinal-obstruction-in-small-animals">Merck\'s '
            'obstruction review</a> describes tissue damage and perforation as additional concerns. Symptoms do not '
            "reliably reveal the bone's location or whether it has passed safely.</p><p>Do not try to push a bone "
            'through with bread, oil or another home remedy. Likewise, do not induce vomiting unless the treating '
            'veterinarian specifically directs it. The professional needs to assess the object and the cat before '
            'choosing an approach. A normal stool or an uneventful meal does not let an owner locate an unseen '
            "fragment. Follow the clinic's advice about examination and follow-up rather than relying on internet "
            'anecdotes about bones passing in other animals.</p><p><a '
            'href="https://www.merckvetmanual.com/digestive-system/surgical-problems-of-the-gastrointestinal-tract-in-small-animals/gastrointestinal-obstruction-in-small-animals">Merck\'s '
            'obstruction review</a> describes vomiting, appetite loss and abdominal pain among possible findings; '
            'symptoms alone cannot locate a swallowed object.</p>'),
           ('Dispose of leftovers before the kitchen is quiet',
            '<p>The highest-risk moment may occur after the meal, when nobody is watching the serving tray. Put '
            'carcasses and scraped bones directly into a closed waste container or another secure place. Clear '
            'roasting pans, sink strainers and plates before leaving the room. Ask visitors not to give the cat '
            'scraps from a plate, even if they first remove the skin or sauce.</p><p>For a cat that enjoys chewing '
            'or food puzzles, ask the veterinary team about suitable enrichment rather than substituting a kitchen '
            'bone. Our <a href="/can-cats-eat/raw-fish/">raw-fish page</a> discusses why raw feeding also raises '
            'separate food-handling questions. The <a href="/guides/how-catcalc-rates-human-foods/">rating guide</a> '
            'distinguishes mechanical injury from calories: a bone is not cleared by being low in energy, '
            'natural-looking or part of an animal-based diet. Choose an appropriate food reward that does not '
            'require the cat to work around an unsafe object.</p>')],
 'dog-food': [('The shared bowl is a nutrition problem when it becomes a habit',
               '<p>A cat stealing a few pieces of a dog’s ordinary food is different from a cat being fed dog food '
               'as its regular ration. The first is usually a question about the amount, ingredients and any '
               'symptoms. The second requires correcting the diet, even when the cat appears to enjoy the food and '
               'its bowl is consistently empty.</p><p><a '
               'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck '
               'Veterinary Manual explains that cats and dogs have different nutritional requirements and that dog '
               'diets can cause deficiencies in cats</a>. The distinction is about the nutrient profile, not whether '
               'the kibble looks similar or contains chicken. Do not use a dog-food bag as the inexpensive permanent '
               'substitute for feline food. If supplies run out, ask the veterinary clinic for a short-term plan '
               'appropriate to the cat rather than assuming that a dog’s ration is nutritionally '
               'interchangeable.</p>'),
              ('Why the same ingredients can produce the wrong diet',
               '<p>An ingredient list can mention meat, grains and vitamins on both dog and cat foods, but the names '
               'do not reveal whether the finished nutrient amounts meet feline requirements. Merck identifies '
               'dietary taurine, arachidonic acid and preformed vitamin A among the important feline differences. '
               'That is why simply comparing the first ingredient or protein percentage does not settle whether a '
               'dog formula is suitable.</p><p><a '
               'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food">FDA '
               'says complete-and-balanced claims refer to established dog or cat nutrient profiles or feeding '
               'procedures</a>. Read which species and life stage the claim names. A product complete for an adult '
               'dog is not thereby complete for a kitten or an adult cat. Our <a '
               'href="/guides/how-to-read-cat-food-labels/">cat-food label guide</a> shows where to find the '
               'adequacy statement so that household foods can be labeled and stored according to their intended '
               'animal.</p>'),
              ('A missing nutrient cannot be fixed with a random topper',
               '<p>Adding a spoonful of tuna, an egg or a vitamin powder to dog food does not turn it into a '
               'professionally balanced feline diet. A deficiency concern involves the whole recipe, not just a '
               'single recognizable nutrient. Too much of an added nutrient can also be undesirable. <a '
               'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
               'advises against supplements without veterinary approval and recommends balanced feline foods unless '
               'a veterinarian prescribes a formulated homemade recipe</a>.</p><p>If dog food has supplied many '
               'meals, tell the veterinarian approximately how long, which product and what else the cat ate. Do not '
               'wait for a visible deficiency to prove that a correction is needed. Compare <a '
               'href="/can-cats-eat/tuna/">tuna</a> and <a href="/can-cats-eat/chicken/">cooked chicken</a> as '
               'optional foods rather than as repair ingredients. A complete feline staple is the practical '
               'replacement, with a transition plan if the cat is reluctant to change.</p>'),
              ('Make separate feeding work in an ordinary household',
               '<p>Start by measuring each animal’s food and watching where it actually goes. Put the dog’s bowl '
               'away after its meal, supervise the feeding period, or use separate rooms if the cat raids it '
               'repeatedly. Avoid leaving an unlimited bowl available simply because both animals can physically eat '
               'the pieces. The aim is to know which animal received which ration, not merely to see that both bowls '
               'eventually became empty.</p><p>Record stolen food in the cat’s daily intake. <a '
               'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA '
               'recommends no more than 10% of feline daily calories from treats</a>, but a treat ceiling is not '
               'permission to plan routine dog-food snacks. Use the <a href="/cat-calorie-calculator/">calorie '
               'calculator</a> to understand how even unplanned extras affect the total. Households with a '
               'prescribed diet need particular care because another animal’s food can disrupt the intended feeding '
               'plan.</p><p>If the animals are fed by different family members, label scoops and storage bins rather '
               'than relying on the shape of the kibble. Write the species, product and measured meal amount where '
               'the person feeding can see them. A simple handover is especially useful when a sitter takes over or '
               'a new bag arrives in similar packaging.</p>'),
              ('Exceptions that make an accidental bite worth a call',
               '<p>Avoid an absolute promise that every bite of every dog product is harmless. “Dog food” may refer '
               'to a raw product, a specialized diet, a treat or food mixed with medication. If the dog’s medication '
               'was in the bowl, contact the prescribing clinic with its name and strength promptly. If raw food was '
               'involved, <a href="https://www.cdc.gov/healthy-pets/about/pet-food-safety.html">CDC’s raw pet-food '
               'warnings</a> apply to microbial hazards regardless of the species pictured on the '
               'package.</p><p>Seek veterinary advice for persistent digestive upset, reduced appetite, weakness or '
               'other abnormal behavior. <a '
               'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell’s '
               'vomiting guidance</a> explains why concurrent signs matter. If a cat refuses feline food but keeps '
               'seeking the dog bowl, report the change rather than assuming that it is simple stubbornness. The <a '
               'href="/guides/senior-cat-weight-and-appetite/">senior weight and appetite guide</a> can help '
               'organize a timeline when appetite changes occur alongside weight loss.</p>')],
 'ham': [('Ham and bacon belong to the processed-food question',
          '<p>A slice of ham is not equivalent to a piece of plain roast meat. Curing, smoking, brining and glazing '
          'can add ingredients, and the composition varies by product. Bacon can also be served with cooking fat or '
          'seasoning, while a holiday ham may be coated in a sweet or savory mixture. Check the actual food rather '
          'than relying on the meat species alone.</p><p><a '
          'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
          'warns about excessively salty foods and identifies onion and garlic as separate hazards</a>. This does '
          'not mean that one stolen crumb of plain ham inevitably causes salt poisoning. It means that product, '
          'quantity and the cat’s circumstances matter. A sandwich filling with onion, a salty brine and a small '
          'piece of unseasoned meat require different discussions. Keep the label or recipe so that a veterinarian '
          'can assess the real exposure.</p><p>Product descriptions such as reduced-sodium or lean are comparisons '
          'with another human food, not feline feeding approvals. Record the actual label rather than relying on the '
          'comparison word. The same applies to a small deli counter sample: if there is no accessible ingredient '
          'list, it is difficult to establish what a cat has received from the product name alone.</p>'),
         ('Do not borrow a dog pancreatitis rule for a cat',
          '<p>Claims that a bacon snack predictably causes feline pancreatitis go beyond the evidence. The <a '
          'href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7995362/">ACVIM consensus statement on pancreatitis in '
          'cats</a> notes that scientific evidence showing dietary fat to be harmful in feline pancreatitis is '
          'lacking and recommends assessing the individual diet and accompanying disease. Cats should not simply '
          'inherit every dietary explanation used for dogs.</p><p>That uncertainty is not a recommendation to feed '
          'bacon. Ham and bacon remain unnecessary extras with variable ingredients and calories. A cat already '
          'being treated for pancreatitis needs the clinic’s own nutrition plan, not a low-fat or high-fat rule '
          'chosen from a general article. If symptoms appear after a meal, report the timing and all foods eaten '
          'without deciding at home that the pancreas must be the cause. A diagnosis requires veterinary '
          'assessment.</p>'),
         ('How to compare a bacon morsel with the daily ration',
          '<p>For a concrete budgeting example, CatCalc uses resting energy requirement, RER = 70 × body weight in '
          'kilograms to the power 0.75. At 3, 4 and 5 kg, that is approximately 160, 198 and 234 kcal before '
          'applying a life-stage or activity factor. With the calculator’s 1.2 neutered-adult factor, the '
          'illustrative totals become about 191, 238 and 281 kcal per day.</p><p>Under <a '
          'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA’s '
          'no-more-than-10% treat guideline</a>, those examples leave roughly 19, 24 and 28 kcal for every extra '
          'combined. They are arithmetic examples, not validated ham servings or a personalized feeding '
          'prescription. A small calorie number does not establish that a salty or seasoned product is appropriate. '
          'Enter the actual circumstances into the <a href="/cat-calorie-calculator/">calorie calculator</a>, and '
          'use a clinic-approved reward rather than filling the maximum allowance with breakfast scraps.</p>'),
         ('The holiday plate contains more than the visible meat',
          '<p>Gravy, stuffing, onion garnish and the cooking liquid may contact a piece before it reaches the cat. '
          'Cutting away the outer glaze does not provide a reliable ingredient history. Similarly, a deli slice '
          'removed from a prepared sandwich can carry sauce or seasoning. If the recipe is unknown, set aside a '
          'suitable cat treat instead of guessing how much flavoring remains.</p><p>For a simpler comparison, see <a '
          'href="/can-cats-eat/chicken/">plain cooked chicken</a> and <a href="/can-cats-eat/turkey/">plain cooked '
          'turkey</a>. Neither should be a complete meal replacement, but a separate unseasoned portion is easier to '
          'assess than cured meat from a mixed plate. <a '
          'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food">FDA '
          'explains why treats and table scraps are not nutritionally complete diets</a>. Giving ham because a cat '
          'is refusing its normal food can hide a developing appetite problem rather than resolve it; our <a '
          'href="/guides/senior-cat-weight-and-appetite/">senior weight and appetite guide</a> lists useful '
          'observations to take to the clinic.</p>'),
         ('After an unattended breakfast raid',
          '<p>Estimate the amount and identify the brand, glaze and any co-ingredients. Note whether packaging, '
          'skewers or bones may also be missing. Do not give salt, oil or a home emetic to try to reverse the '
          'incident. Contact your veterinarian promptly if a hazardous ingredient was involved or the amount is '
          'substantial or unclear.</p><p><a '
          'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell '
          'advises evaluation for vomiting with weakness, lethargy, reduced appetite, blood or diarrhea</a>. Marked '
          'thirst or neurological signs after a very salty exposure also merit prompt professional advice under '
          'ASPCA’s salt guidance. Avoid treating a normal first hour as proof that the whole plate was harmless. For '
          'routine prevention, ask everyone in the household to stop dropping scraps while cooking and put breakfast '
          'waste in a container the cat cannot open.</p>')],
 'avocado': [('Why animal-wide avocado warnings need context',
              '<p>Avocado appears on many broad pet-hazard lists, but species matters when interpreting them. <a '
              'href="https://www.aspca.org/news/scoop-avocado-and-your-pets">ASPCA\'s avocado explanation</a> '
              'emphasizes severe sensitivity in certain birds and other animals. Those effects should not simply be '
              'copied into a prediction of heart damage or death in every cat that licks a little avocado '
              'flesh.</p><p>The <a '
              'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/potentially-dangerous-items-your-pet">FDA\'s '
              'pet-hazard page</a> likewise distinguishes milder toxicity in cats and dogs from severe effects in '
              'more sensitive species. CatCalc advises against deliberately feeding avocado without pretending that '
              'all exposures are equivalent. If an accident occurs, identify which part of the fruit was involved '
              'and ask a veterinarian about that event. Our <a href="/guides/how-catcalc-rates-human-foods/">rating '
              'method</a> separates limited species-specific evidence from established mechanical and ingredient '
              'hazards, so the recommendation can remain cautious without inventing a feline toxic dose.</p>'),
             ('A missing pit is a different problem from a smear of flesh',
              '<p>The <a '
              'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/potentially-dangerous-items-your-pet">FDA '
              'guidance</a> identifies avocado pits as a potential gastrointestinal obstruction hazard. A pit or a '
              'piece of one should therefore be reported separately from the flesh. Whether a cat could swallow the '
              'whole pit is not the only question: describe any chewing, broken pieces and missing material so the '
              'clinician can assess what might have happened.</p><p>Keep the remaining pit or photograph it beside '
              'an ordinary size reference. State whether the cat was witnessed chewing it or was merely found near '
              'discarded fruit. If skin or packaging is also missing, mention that rather than assuming every absent '
              'piece was eaten. Store discarded pits where the cat cannot retrieve them from the counter or waste '
              'bin. Removing the flesh for a human meal does not complete the pet-safety part of kitchen '
              'cleanup.</p>'),
             ('Guacamole should be assessed as a recipe',
              '<p>A bowl of guacamole can contain several ingredients besides avocado. Check for <a '
              'href="/can-cats-eat/onions/">onion</a>, <a href="/can-cats-eat/garlic/">garlic</a> and other '
              'additions, and save the label if the dip is purchased. A lick of a prepared dip should not be '
              'described to the clinic as plain avocado if its ingredients are unknown.</p><p>The same principle '
              'applies to avocado toast and restaurant salads. Identify the bread, spread, dressing and garnish '
              'rather than concentrating on the most visible ingredient. Our <a href="/can-cats-eat/bread/">bread '
              'page</a> explains why a plain baked product is different from a seasoned or mixed one. Do not remove '
              'visible onion pieces and assume the remaining dip is now suitable to share. Plan any appropriate cat '
              'treat separately before preparing the human dish, so there is no need to judge a spoonful from a '
              'mixed bowl at the table.</p>'),
             ('An exposure history should identify uncertainty, not hide it',
              '<p><a href="https://www.aspca.org/news/scoop-avocado-and-your-pets">ASPCA recommends recording the '
              'amount and seeking veterinary advice after suspected avocado ingestion</a>. Provide the approximate '
              "time, the part of the fruit or product eaten and the cat's weight. Tell the team about any symptoms "
              'and existing health conditions. An estimate such as a smear from a spoon is more informative than '
              'saying the cat had an avocado, which could mean anything from a lick to access to discarded '
              'parts.</p><p>Seek urgent care for choking, breathing difficulty, collapse, repeated vomiting or '
              'marked abdominal discomfort. These signs need attention even if avocado is not ultimately the cause. '
              'A cat appearing well does not reveal whether a swallowed object is present. Ask the clinic whether '
              'observation or examination is appropriate; do not use a list of severe signs as permission to '
              'postpone the initial advice call until the cat becomes obviously ill.</p><p>For the separate '
              'swallowed-object concern, <a '
              'href="https://www.merckvetmanual.com/digestive-system/surgical-problems-of-the-gastrointestinal-tract-in-small-animals/gastrointestinal-obstruction-in-small-animals">Merck '
              'describes gastrointestinal obstruction signs</a> including vomiting, appetite loss and abdominal '
              'pain.</p>'),
             ('There is no need to find an avocado serving for cats',
              "<p>Avocado's popularity in human meals does not establish a nutritional requirement for a cat. A "
              'complete feline diet is the everyday feeding plan; an optional treat does not need to resemble a '
              'human healthy-fat trend. If a veterinarian has prescribed a particular diet, discuss extras with that '
              'team rather than adding avocado to change its fat content.</p><p>Use the <a '
              'href="/cat-calorie-calculator/">calorie calculator</a> to organize appropriate food energy, not to '
              'assess persin or a pit. Fitting an ingredient into a calorie allowance does not resolve an '
              'obstruction or toxicology question. For household prevention, clear cut fruit, wash utensils and '
              'close the bin before the cat returns to the preparation area. Ask guests to keep dips and discarded '
              'pits away from pets. This handles the realistic exposure routes without requiring an unsupported '
              'claim that a particular number of grams is universally safe or dangerous for every cat.</p>')],
 'peanut-butter': [('A useful dog reward is not automatically a useful cat reward',
                    '<p>Peanut butter is often discussed in dog training, so it can appear on lists of pet treats '
                    'without a separate feline assessment. Cats have different nutritional needs and may have no '
                    'interest in it. There is no requirement to introduce peanut butter, and refusing it does not '
                    'indicate that the cat is missing an important food group.</p><p><a '
                    'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
                    'describes cats as obligate carnivores that need a balanced supply of nutrients</a>. Peanut '
                    'butter should not be used as a protein substitute for a complete feline diet. A product can '
                    'contain protein and still have the wrong role in the feeding plan. If you need a reward for '
                    'training or a food for medication, ask whether part of the regular ration or a clinic-approved '
                    'alternative would do the job more simply.</p>'),
                   ('Read the sweetener name and keep the species distinction',
                    '<p>Check the entire ingredient list before considering any taste. Peanut butter products '
                    'differ, and sweetened or flavored versions may contain ingredients absent from a plain jar. '
                    'Xylitol is especially important to identify because dog poisoning information is widely '
                    'repeated without a feline qualification.</p><p><a '
                    'href="https://www.aspcapro.org/resource/most-common-sleep-aid-toxicities-cats-and-dogs">ASPCApro '
                    'describes gastrointestinal upset from xylitol in cats</a>; the classic canine low-blood-sugar '
                    'and liver-injury pattern should not be asserted as an established feline outcome. Limited '
                    'feline evidence also does not validate feeding xylitol products intentionally. Our <a '
                    'href="/can-cats-eat/xylitol/">xylitol page</a> explains that uncertainty. Chocolate-flavored '
                    'peanut spreads raise an additional, independent hazard covered on the <a '
                    'href="/can-cats-eat/chocolate/">chocolate page</a>. If an unknown spread was eaten, provide the '
                    'actual ingredient list to the veterinarian instead of reporting only that the cat ate '
                    'peanuts.</p><p>Check again when buying a replacement jar, even if its brand is familiar. '
                    'Products within the same brand can have different recipes, and a flavored spread may share a '
                    'similar-looking label with plain peanut butter. For a household food used with medication, '
                    'keeping the ingredient panel and clinic instructions together helps prevent a later '
                    'substitution based only on the jar’s color.</p>'),
                   ('Texture and food delivery deserve attention',
                    '<p>A thick sticky dollop is an awkward way to reward a small animal. Do not spread peanut '
                    'butter deep inside an object that the cat cannot comfortably reach, force a lump into the '
                    'mouth, or assume that licking it will be a suitable enrichment task for every cat. The '
                    'practical aim of a reward is easy, voluntary consumption; peanut butter is unnecessary when it '
                    'makes that task more difficult.</p><p>Medication adds another reason to ask the clinic. Check '
                    'whether the specific drug may be given with food, and do not crush or open it without '
                    'instructions. A cat can lick the food and leave a tablet behind, so the presence of a favorite '
                    'spread does not establish that treatment succeeded. Compare <a '
                    'href="/can-cats-eat/chicken/">plain cooked chicken</a> or a designated feline medication treat '
                    'only after confirming that the alternative fits the prescription and diet.</p>'),
                   ('Measure calories before describing a portion as tiny',
                    '<p>Peanut butter is an energy-dense food, and a human spoonful is not a useful feline serving '
                    'rule. Read the jar’s calorie declaration and serving weight rather than judging by the apparent '
                    'size of the smear. Divide the energy by the labeled gram weight if you need a per-gram value, '
                    'then count any suitable portion alongside all other extras.</p><p><a '
                    'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA '
                    'recommends no more than 10% of daily calories from all treats</a>. Use the <a '
                    'href="/cat-calorie-calculator/">calorie calculator</a> as a starting estimate for the day’s '
                    'energy target, not as a safety certificate for peanut butter. The maximum treat budget is not '
                    'an amount the cat ought to receive. A prescribed diet or prior poor tolerance can make an '
                    'otherwise small reward inappropriate. The <a '
                    'href="/guides/how-to-read-cat-food-labels/">cat-food label guide</a> also helps distinguish '
                    'nutritional adequacy from an attractive ingredient or marketing claim.</p>'),
                   ('What a stolen lick does and does not tell you',
                    '<p>Remove the jar, check what kind of spread it contains, and estimate the amount. One '
                    'uneventful lick is not proof that repeated servings will suit the cat, but it also should not '
                    'be described automatically as a severe poisoning. The relevant next step depends on '
                    'ingredients, amount and symptoms. Keep the label available if you contact your veterinarian or '
                    'poison-control service.</p><p><a '
                    'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell '
                    'recommends prompt assessment when vomiting is accompanied by weakness, lethargy, reduced '
                    'appetite, blood or diarrhea</a>. Trouble swallowing or abnormal breathing after any food needs '
                    'urgent attention. Do not keep offering the spread to test whether a reaction repeats. For '
                    'routine care, select an easily measured reward that works with the cat’s established ration and '
                    'medical plan. Peanut butter can be omitted entirely without leaving a nutritional gap in a '
                    'complete feline diet.</p>')],
 'bread': [('Fully baked bread and proofing dough are different questions',
            '<p>The <a href="https://www.aspcapro.org/resource/bread-ingestion-pets">ASPCApro bread-ingestion '
            'guidance</a> distinguishes a small occasional serving of fully baked plain bread from raw yeast dough. '
            'Yeast-based dough can keep expanding and fermenting after ingestion, creating hazards that do not '
            'describe an ordinary cooled slice. If the food was partly baked, still proofing or taken from a '
            'bread-machine pan, tell the veterinarian exactly that rather than calling it bread.</p><p>Our <a '
            'href="/can-cats-eat/raw-dough/">raw-dough page</a> addresses the urgent expansion-and-alcohol concern. '
            'Do not offer a raw scrap while shaping a loaf or let the cat lick an unbaked mixing bowl. Keep dough '
            'inaccessible throughout proofing, not just while ingredients are being mixed. Once bread is fully '
            "baked, it still needs an ingredient check and should not become the cat's regular meal or an excuse to "
            'share every bakery product.</p>'),
           ('Read past the word bread on the label',
            '<p>A bread name may describe flavor rather than a complete recipe. Raisin loaf belongs in the <a '
            'href="/can-cats-eat/raisins/">raisin discussion</a>, and garlic bread needs the <a '
            'href="/can-cats-eat/garlic/">garlic warning</a>. Chocolate chips, onion toppings and alcohol-containing '
            'fillings introduce other questions. Save the ingredient label when asking about an accidental ingestion '
            'instead of assuming the bread portion determines the whole risk.</p><p>The <a '
            'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
            'people-food guidance</a> identifies several of these ingredients as household concerns and specifies '
            'that grape-related kidney toxicity is established in dogs. That species distinction still matters when '
            'a raisin is baked into bread. A mixed product should be assessed honestly rather than declared harmless '
            'because it has been heated, or catastrophically poisonous to cats using a statement established only in '
            'another species. If you do not know the recipe, explain that uncertainty to the clinic.</p>'),
           ('A snack needs a place inside the feeding allowance',
            '<p>The <a href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA '
            'cat-treat guidance</a> limits all treats together to no more than ten percent of daily calories for an '
            'appropriate healthy-cat feeding plan. This is a ceiling for extras, not a target to fill with bread. A '
            "cat's main food should remain a complete diet appropriate to its circumstances, and a medical diet may "
            'leave no room for an unapproved extra.</p><p>Bread products vary, so do not borrow a calorie figure '
            'from an unrelated loaf. If you choose to offer an occasional tiny piece, use the actual label and '
            'account for every other treat that day. The <a href="/cat-calorie-calculator/">calorie calculator</a> '
            'explains the RER-based estimate used by CatCalc; it does not turn an energy allowance into proof that a '
            'recipe is safe. Ingredient suitability comes first, then portion accounting for a food that is '
            'appropriate at all.</p>'),
           ('Do not use bread as a home treatment',
            '<p>Bread is sometimes suggested informally to push a swallowed bone through or settle an unknown '
            'digestive problem. Do not use that advice instead of a veterinary assessment. The <a '
            'href="/can-cats-eat/bones/">bone page</a> explains the injury and obstruction concern, which is not '
            'resolved by adding another food. Tell the clinic what the cat swallowed and follow its specific '
            'directions.</p><p>Likewise, ongoing vomiting, diarrhea or refusal of normal food needs veterinary '
            'attention rather than a bread-based diet experiment. If a change followed a bakery product, keep the '
            'packaging and describe the amount and time. Distinguish a digestive complaint from signs of choking or '
            'difficulty breathing, which require emergency care. A food being acceptable as an occasional treat does '
            'not establish it as treatment, and an apparently mild symptom does not identify which ingredient or '
            'unrelated problem caused it.</p>'),
           ('Make plain mean plain at the table',
            '<p>If sharing a suitable baked crumb, set it aside before adding butter, dip or a seasoned spread. Do '
            'not take a supposedly clean corner from a plate covered in sauce and assume that it matches a plain '
            "loaf. A household rule of using the cat's own food for rewards is often easier than reviewing every "
            'topping during breakfast.</p><p>Put bread bags, ties and wrappers away when the meal ends, and keep '
            'proofing dough separately secured. Ask children and visitors to check before feeding bakery leftovers, '
            'especially items with visible fruit or chocolate. There is no need to persuade a cat to eat bread or to '
            'replace a rejected treat with a richer version. Our <a '
            'href="/guides/how-catcalc-rates-human-foods/">food-rating guide</a> explains why a modest permission '
            'for a plain preparation never extends automatically to every product sold under the same food '
            'name.</p>')],
 'banana': [('A banana taste is optional, not a potassium prescription',
             "<p>The familiar idea of a banana as a healthy human snack is a poor reason to add it to a cat's meals. "
             'A cat eating a complete diet does not need a piece of fruit merely because people associate that fruit '
             'with a particular vitamin or mineral. <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/banana">ASPCA '
             'lists the banana plant as non-toxic to cats</a>; that is a toxicity classification, not evidence that '
             'banana treats improve feline health or an instruction to feed them every day.</p><p>If your cat is '
             'curious about ripe banana, you can consider a small taste of peeled flesh within its existing treat '
             'allowance. Equally, there is no problem with choosing a familiar feline reward instead. Do not buy '
             'supplements or start feeding banana to correct suspected low potassium: a medical question about '
             'minerals needs measurements and veterinary advice rather than a kitchen experiment.</p>'),
            ('The peel, a thick coin and a soft smear',
             '<p>Preparation is mostly about keeping the experiment small and manageable. Take the peel away '
             'completely and discard it before letting the cat approach. Separate a tiny amount of ripe flesh with a '
             'clean utensil rather than offering a thick round slice from your hand. A small soft smear on a dish is '
             'easier to inspect than a mouthful the cat grabs while competing with another pet. This is a practical '
             'choice, not a scientifically established safe dose.</p><p>The <a '
             'href="https://www.petpoisonhelpline.com/uncategorized/pet-friendly-human-food/">Pet Poison Helpline\'s '
             'produce article</a> includes bananas among foods that may be offered to healthy pets, while asking '
             "owners to consider the individual animal's health. That qualification matters. A cat on a therapeutic "
             'diet, with ongoing digestive symptoms or with specific feeding instructions should not be enrolled in '
             'a new snack trial simply because a plant appears on a non-toxic list.</p>'),
            ('Banana bread is a recipe, not a fruit serving',
             '<p>Before sharing any baked product, put the fruit name aside and read the complete ingredient list. '
             'Banana bread can also contain <a href="/can-cats-eat/chocolate/">chocolate</a>, <a '
             'href="/can-cats-eat/raisins/">raisins</a>, nuts or sweeteners. The amount of banana in the loaf cannot '
             'cancel a concern about another ingredient. The <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
             'people-foods guidance</a> covers several of these hazards. Its dog-focused xylitol warnings should not '
             'be copied into a claim that feline toxic doses are known; our <a href="/can-cats-eat/xylitol/">xylitol '
             'page</a> explains that evidence limit.</p><p>Banana chips, flavored milk, smoothies and desserts also '
             'deserve their own checks. A smooth texture does not make a drink suitable for a cat. If you cannot '
             'identify every ingredient in a café product, keep it for people rather than testing it on the cat. '
             'Plain peeled fruit is easier to reason about than a complicated treat.</p>'),
            ('A small body has a small extra-food allowance',
             '<p>Weight alone does not produce a banana portion. The <a href="/cat-calorie-calculator/">calorie '
             'calculator</a> starts with resting energy requirement and applies a life-stage factor, so the same '
             'body weight can produce different daily targets. For example, selecting the neutered-adult factor of '
             '1.2 gives approximately 191 kcal for 3 kg, 238 kcal for 4 kg and 281 kcal for 5 kg. These are rounded '
             'planning estimates, not a prescription.</p><p>If a clinician accepts that estimate and a ten-percent '
             'ceiling for all treats, that means roughly 19, 24 or 28 kcal available across every extra food '
             'combined. It does not mean banana should supply that much. <a '
             'href="https://vcahospitals.com/know-your-pet/cat-treats">VCA explains the treat-budget principle</a>. '
             'Use a measured product value if converting a weighed portion to calories; do not multiply an assumed '
             'banana size by an invented energy value. The smallest useful taste is often simpler than calculating a '
             'generous serving.</p><p>The exponential RER formula and neutered-adult factor used here are described '
             'in <a '
             'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck\'s '
             'energy reference</a>; <a '
             'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA supports '
             'the ten-percent treat ceiling</a>, rather than these particular rounded daily estimates.</p>'),
            ('When to leave fruit out of the discussion',
             '<p>A cat refusing its usual food does not need a succession of tempting fruit samples. Keep the '
             'feeding history clear and call your veterinarian when appetite changes persist or accompany weight '
             'loss. Cornell warns that <a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">food '
             'refusal and weight loss warrant assessment</a>. A banana accepted during that period does not show '
             "that the cat's normal nutrition is adequate or that the underlying problem has resolved.</p><p>After a "
             'first taste, discontinue it if vomiting or loose stool appears and tell the clinic what else changed '
             'that day. Breathing difficulty, collapse or inability to swallow requires urgent care. For a cat that '
             'remains comfortable but uninterested, just remove the uneaten fruit. You do not need to persuade it '
             'that fruit is enjoyable. Compare the preparation notes for <a href="/can-cats-eat/apples/">apple '
             'flesh</a> only if there is a real reason to offer a different optional snack.</p>')],
 'apples': [('The edible slice and the discarded core are different questions',
             '<p>A cat investigating an apple slice is not facing the same exposure as a cat chewing a core, leaves '
             'or a fallen branch. The <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/apple">ASPCA '
             'apple entry</a> identifies cyanogenic compounds in seeds, stems and leaves. That distinction is the '
             'reason for careful preparation; it does not mean a sliver of clean apple flesh has the same risk as '
             'plant material. Remove the entire core rather than picking out the seeds you can see. Keep the '
             "discarded parts in a covered bin before putting a taste on the cat's dish.</p><p>For a healthy cat "
             'already allowed optional treats, our practical approach is a very small, thin piece of flesh, peeled '
             'if that makes it easier to inspect. This is an editorial serving suggestion, not a toxicology '
             'threshold. Do not use the absence of immediate symptoms to establish a safe seed count.</p>'),
            ('Fresh, softened, dried or sauced',
             '<p>Fresh apple is easiest to assess because there is only one ingredient. Wash the outside before '
             'cutting, use a clean knife and cut a small piece that does not require gnawing on a hard wedge. A '
             'little apple softened in plain water is another way to avoid a firm chunk; cool it before offering it. '
             'None of this requires cinnamon, butter, honey or a dessert topping. Do not put a whole apple down as a '
             'chew toy.</p><p>Apple sauce needs an ingredient check even if the front says natural. Apple pie, '
             'caramel apples and dried fruit mixes are separate recipes, and an apple flavor does not tell you what '
             'else is present. A mix containing <a href="/can-cats-eat/raisins/">raisins</a> belongs under the '
             'raisin advice. The <a '
             'href="https://www.petpoisonhelpline.com/uncategorized/pet-friendly-human-food/">Pet Poison Helpline\'s '
             'veterinarian-written produce guidance</a> includes apple slices without the core among optional pet '
             'snacks, rather than endorsing every apple-containing food.</p>'),
            ('Why a vitamin reputation is not a feeding plan',
             '<p>People often choose apples for their own snacks and assume the same health argument transfers to '
             "cats. That skips the more useful question: what does the cat's current food already provide? A "
             'complete feline diet is designed around feline requirements, while an apple is an extra ingredient. '
             'The <a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
             "feeding guide</a> explains cats' reliance on animal-derived nutrients. Adding fruit is therefore a "
             'preference to accommodate, not a missing step in balanced feeding.</p><p>Use the <a '
             'href="/guides/how-to-read-cat-food-labels/">food-label guide</a> to check the main diet before '
             'worrying about fruit variety. If you are choosing between apple and <a '
             'href="/can-cats-eat/banana/">banana</a>, there is no need to make either a daily requirement. A '
             "familiar portion of the cat's own food may make a simpler reward, especially when several household "
             'members hand out snacks.</p>'),
            ('Count the whole day, including the training treats',
             '<p>An apple taste does not create a separate allowance on top of other extras. List dental treats, '
             'food used for tablets, scraps and rewards together. The <a '
             'href="https://vcahospitals.com/know-your-pet/cat-treats">VCA treat guide</a> uses a limit of about ten '
             'percent of daily energy from treats; a smaller amount or no extras may suit an individual cat. The '
             'ceiling is not a challenge to finish a bowl of fruit.</p><p>Open the <a '
             'href="/cat-calorie-calculator/">calorie calculator</a> for a starting daily estimate, then use the '
             "food's actual energy information if you intend to measure it. The tool cannot convert a phrase such as "
             'one slice into reliable calories because slices vary. Keep any apple trial easy to observe: offer it '
             'separately, note what was eaten and avoid adding several unfamiliar foods at the same sitting.</p>'),
            ('After an unplanned bite',
             '<p>If the cat ate only a little prepared flesh and remains well, stop offering more and watch its '
             'normal eating and litter-box habits. If seeds, a core, leaves or an unknown apple dessert were '
             'involved, contact your veterinarian with those details instead of treating every exposure as '
             'identical. Keep the packaging or photograph the plant material. Difficulty breathing, collapse or '
             'choking calls for emergency care; do not wait for a reply to a website.</p><p>Vomiting, diarrhea, '
             'abdominal discomfort or appetite loss are signs to discuss with a veterinarian, especially when '
             'repeated or accompanied by reduced activity. <a '
             'href="https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats">Merck\'s '
             'digestive-disorder overview</a> describes these as clinical signs with multiple possible causes. They '
             'do not prove an apple allergy, and swapping immediately to another fruit can make the history harder '
             'to interpret. Give the clinic the timeline, amount and any other foods eaten.</p>')],
 'turkey': [('Decide what the cat will receive before carving starts',
             '<p>A holiday turkey often reaches the table surrounded by foods that should not reach the cat’s bowl. '
             'Rather than rescuing a piece from a crowded platter, set aside an unseasoned boneless portion while '
             'preparing the meal. The useful distinction is a separate piece of cooked meat versus a sample of the '
             'human recipe, not white meat versus a particular holiday tradition.</p><p>Check whether the bird was '
             'injected, brined, marinated or supplied with a seasoning solution. The outer surface is not the only '
             'possible source of added ingredients. If the recipe is unknown, a regular feline treat is a clearer '
             'choice. <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
             'identifies onion and garlic as feline hazards</a>; removing visible stuffing does not prove that a '
             'carved piece was never in contact with seasoned juices.</p>'),
            ('Roasting safety and serving safety are separate checks',
             '<p>The bird must be cooked properly, then the cat’s portion must be served appropriately. <a '
             'href="https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling">FDA specifies 165°F for '
             'poultry and stuffing</a>; use a thermometer and follow food-handling directions. Let the separate '
             'portion cool, remove all bones, and cut or shred it into manageable pieces. Do not hand over a hot '
             'carving-board scrap merely because the cat is waiting beside you.</p><p>The preparation area also '
             'needs attention. Keep raw juices, packaging, carving tools and discarded bones inaccessible. <a '
             'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA warns that '
             'both raw and cooked bones can cause serious injury when cats chew or ingest them</a>. Our <a '
             'href="/can-cats-eat/bones/">bone guidance</a> covers why a turkey leg or carcass is not an enrichment '
             'toy. A closed rubbish container matters after the meal as much as supervision during carving.</p>'),
            ('Stuffing and gravy are different foods',
             '<p>A piece of turkey covered in gravy carries the gravy recipe with it. Stuffing may contain onions, '
             'garlic, raisins or other ingredients that change the exposure. These are not minor details to omit '
             'when calling a clinic. Keep the recipe or packaging and describe what the cat could have reached, '
             'including garnish and sauces.</p><p>Read the <a href="/can-cats-eat/onions/">onion page</a> and <a '
             'href="/can-cats-eat/raisins/">raisin page</a> for the relevant differences in evidence and response. '
             'ASPCA’s food-hazard guidance supports avoiding Allium ingredients, while grape and raisin advice must '
             'not assume that canine dose information is established for cats. Do not turn “holiday leftovers” into '
             'a single safe category. Plain turkey, a gravy-soaked piece and a bowl of stuffing have different '
             'ingredient lists even when served from the same plate.</p><p>Tell guests in advance that the cat '
             'already has its own measured food. Otherwise each person may offer what looks like one harmless morsel '
             'while the total intake and ingredient history become impossible to reconstruct. Put the reserved plain '
             'portion in a separate labeled container instead of leaving it on the carving board among gravy, skin '
             'and stuffing scraps.</p>'),
            ('Why a meat-loving cat still needs its ordinary food',
             '<p>Turkey supplies an animal-food ingredient, but the presence of protein does not certify a balanced '
             'diet. <a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
             'explains that cats need a range of vitamins, minerals, amino acids and fatty acids in appropriate '
             'amounts</a>. A turkey-only menu, or a homemade mixture assembled from holiday leftovers, does not '
             'establish that balance. Continue the complete feline diet rather than replacing dinner with a large '
             'serving of roast meat.</p><p>For a suitable occasional reward, <a '
             'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA recommends '
             'no more than 10% of daily calories from treats</a>. Count turkey alongside every other extra, using '
             'the <a href="/cat-calorie-calculator/">calorie calculator</a> to understand the overall energy '
             'allowance. This ceiling does not establish a safe number of slices or a clinical feeding prescription. '
             'The <a href="/guides/how-to-read-cat-food-labels/">cat-food label guide</a> helps compare complete '
             'turkey-based cat food with supplementary products and plain meat. See <a '
             'href="/can-cats-eat/chicken/">cooked chicken</a> for another single-ingredient reward that needs the '
             'same nutritional boundary.</p>'),
            ('An appetite change deserves more than a better leftover',
             '<p>If a cat abruptly refuses its usual food but accepts turkey, do not assume that the problem is '
             'merely a preference for festive cooking. Record when appetite changed, how much complete food was '
             'eaten and whether weight or behavior has changed. A favorite meat can obscure a reduced overall intake '
             'when nobody is measuring it.</p><p><a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell '
             'recommends prompt evaluation for vomiting with weakness, lethargy, reduced appetite, blood or '
             'accompanying diarrhea</a>. Contact the clinic after a concerning exposure rather than waiting to see '
             'whether another turkey portion stays down. For older cats, the <a '
             'href="/guides/senior-cat-weight-and-appetite/">senior weight and appetite guide</a> offers a simple '
             'way to organize relevant observations. Turkey can remain a limited reward for an otherwise suitable '
             'cat, but it cannot replace a medical assessment, a balanced ration or safe food handling.</p>')],
 'salmon': [('Cooked salmon is an ingredient, not a fish-oil prescription',
             '<p>Salmon can be appealing as an occasional piece of cooked fish, but broad claims about skin, joints '
             'or inflammation should not be attached to an unmeasured kitchen serving. A nutrient associated with an '
             'ingredient does not establish a therapeutic dose or a clinical result for a cat. If your veterinarian '
             'recommends an omega-3 product, ask for that product and dosing plan instead of substituting extra '
             'fish.</p><p><a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
             'stresses that feline diets need nutrients in appropriate amounts and that supplements should not be '
             'added without veterinary approval</a>. A complete food containing salmon and a plate of salmon flesh '
             'therefore serve different purposes. Use the <a href="/guides/how-to-read-cat-food-labels/">cat-food '
             'label guide</a> to check nutritional adequacy on the cat-food package. Plain fish can be an extra when '
             'suitable; it does not provide the whole nutritional foundation by itself.</p>'),
            ('Start with the cooking method, then inspect for bones',
             '<p>Cook a separate unseasoned portion and use clean utensils to remove the cat’s share. <a '
             'href="https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling">FDA gives 145°F for fin '
             'fish, or flesh that is opaque and separates easily with a fork</a>. After cooking, inspect carefully '
             'for bones and let the food cool. Flake it onto a clean surface where small bones are easier to notice '
             'rather than feeding directly from a large fillet.</p><p>Do not assume that a boneless label replaces '
             'your own inspection. A cat that gulps food still needs manageable pieces. <a '
             'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA warns that '
             'bones can injure cats or cause obstruction</a>; fish bones are not a calcium supplement. If a bone may '
             'have been swallowed and the cat is gagging, drooling or behaving abnormally, contact a veterinarian '
             'instead of offering bread or another bulky food to “push it through.”</p><p>Take time to check the '
             'thin end and edges of a fillet as well as the center. Work under good light, separate the flakes and '
             'discard anything uncertain. This inspection is a preparation precaution, not a guarantee against every '
             'small bone. If checking the portion is difficult, choosing another approved reward is more sensible '
             'than relying on the package photograph.</p>'),
            ('Smoked, cured and glazed fish do not belong in the same category',
             '<p>A smoked slice, a teriyaki fillet and a plain cooked portion have different recipes. Check salt, '
             'seasonings and sauces rather than treating every pink piece as equivalent. Garlic butter and '
             'onion-containing sauces remain hazards after the fish has been heated. <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
             'identifies Allium ingredients as causes of red blood cell damage in cats</a>. Scraping off the obvious '
             'sauce cannot certify that the rest of the portion is unseasoned.</p><p>Read <a '
             'href="/can-cats-eat/garlic/">garlic guidance</a> if a seasoned dish was eaten. Sushi, lightly seared '
             'preparations and raw fish trimmings raise a different food-safety question, discussed on the <a '
             'href="/can-cats-eat/raw-fish/">raw-fish page</a>. For routine sharing, a separately cooked piece with '
             'a known ingredient history is easier to assess than a restaurant leftover, smoked platter or mixed '
             'seafood dish.</p>'),
            ('A fish reward should leave the main diet intact',
             '<p>A cat can prefer salmon strongly enough that owners keep increasing the topping. Measure how much '
             'complete food is actually eaten, particularly if the fish has begun replacing rather than accompanying '
             'it. <a '
             'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food">FDA '
             'explains that treats and supplements are generally not intended as a sole balanced diet</a>. '
             'Preference does not demonstrate that the overall menu has become nutritionally adequate.</p><p>Use <a '
             'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA’s maximum '
             'of 10% of daily calories from all treats</a> as a ceiling for extras, not a recommendation to offer '
             'that much salmon. The <a href="/cat-calorie-calculator/">calorie calculator</a> helps estimate the '
             'day’s energy target, but an individual medical plan takes priority. A piece that fits the calorie '
             'budget may still be unsuitable during a diet trial or for another clinical reason. Compare <a '
             'href="/can-cats-eat/tuna/">tuna</a> and <a href="/can-cats-eat/shrimp/">cooked shrimp</a> as separate '
             'foods with separate preparation details rather than interchangeable free additions.</p>'),
            ('Keep the exposure history clear if illness occurs',
             '<p>If the cat develops digestive upset, keep the package or recipe and record the amount, cooking '
             'method and timing. Include all sauces and other seafood in the dish. Do not decide that fish allergy, '
             'food poisoning or a bone must be responsible solely because salmon was the newest food; the clinic '
             'needs enough information to assess alternatives.</p><p><a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell '
             'advises prompt veterinary evaluation when vomiting occurs with weakness, lethargy, reduced appetite, '
             'blood or diarrhea</a>. A cat repeatedly refusing its normal meals also needs attention even when it '
             'still accepts salmon. The <a href="/guides/senior-cat-weight-and-appetite/">senior weight and appetite '
             'guide</a> helps organize weight and appetite changes for an appointment. Stop the new reward while '
             'seeking advice, and do not use home supplements, oil or additional fish to try to correct an '
             'unexplained symptom.</p>')],
 'shrimp': [('The shrimp name does not describe the dish',
             '<p>A shrimp taken from a garlic-butter pan is a different food from a shrimp cooked alone. Restaurant '
             'scampi, fried shrimp, cocktail platters and ready-to-eat salads can introduce ingredients beyond the '
             'seafood itself. Before sharing, identify how the food was cooked and what touched it, including sauces '
             'served underneath or alongside it.</p><p><a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
             'identifies onion and garlic as causes of red blood cell damage in cats</a>. Removing a visible garlic '
             'piece does not establish that the shrimp is plain. If a seasoned dish was eaten, keep the recipe or '
             'package and consult the <a href="/can-cats-eat/garlic/">garlic page</a> for the information the '
             'veterinary team needs. For a planned reward, a separate unseasoned piece is simpler than trying to '
             'rinse a finished human dish into suitability.</p><p>Be particularly clear about ready-cooked products: '
             'already cooked describes heat treatment, while plain describes ingredients. A chilled shrimp from a '
             'deli platter may satisfy the first description without satisfying the second. Keep the package until '
             'the reward is finished, and distinguish the shrimp from the dipping sauce when explaining exactly what '
             'the cat could have eaten.</p>'),
            ('Cook the flesh and discard the shell before portioning',
             '<p>Use cooked shrimp, remove the head, shell and tail, and cut the flesh into small manageable pieces. '
             'This is a practical preparation approach rather than a validated feline serving protocol. Do not give '
             'the cat a hard tail to chew while the rest of dinner is prepared. The shell and tail are not useful '
             'nutritional additions that need to be preserved.</p><p><a '
             'href="https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling">FDA’s food-handling '
             'guidance describes cooked shrimp flesh as pearly and opaque</a>. Follow package cooking instructions '
             'and safe storage practices, and let the cat’s portion cool. A pink color alone is not the entire '
             'ingredient or handling history of a prepared product. Raw seafood raises a separate pathogen question: '
             '<a href="https://www.cdc.gov/healthy-pets/about/pet-food-safety.html">CDC advises against raw animal '
             'treats because they can carry harmful germs</a>. See <a href="/can-cats-eat/raw-fish/">raw-fish '
             'guidance</a> for the broader distinction between cooked seafood and raw feeding.</p>'),
            ('A small seafood reward is not a mineral supplement',
             '<p>Shrimp can be appealing without being required for a balanced feline diet. Do not assume that trace '
             'nutrients in an ingredient make it a useful treatment for a deficiency or a reason to add it every '
             'day. <a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
             'explains that cats need a carefully balanced range of nutrients and that more vitamins or minerals are '
             'not necessarily better</a>. A complete food already aims to supply the required '
             'balance.</p><p>Likewise, shrimp flesh alone is not a complete meal simply because it is animal '
             'protein. <a '
             'href="https://www.fda.gov/animal-veterinary/animal-health-literacy/complete-and-balanced-pet-food">FDA '
             'distinguishes complete-and-balanced pet food from treats and supplementary foods</a>. If you want a '
             'seafood-based staple, assess the cat food’s adequacy statement instead of assembling a bowl from plain '
             'shellfish. The <a href="/guides/how-to-read-cat-food-labels/">cat-food label guide</a> helps locate '
             'the relevant wording. Avoid replacing complete meals with shrimp when the cat becomes enthusiastic '
             'about its smell.</p>'),
            ('Use measured extras rather than a shrimp-count rule',
             '<p>Shrimp vary greatly in size, so “one shrimp” is a poor universal portion description. Cut the '
             'reward before offering it and count its energy with the day’s other extras. A kitchen scale and '
             'relevant product information are more useful for budgeting than a photograph of a serving intended for '
             'another cat.</p><p><a '
             'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA recommends '
             'that all treats together supply no more than 10% of daily calories</a>. The <a '
             'href="/cat-calorie-calculator/">calorie calculator</a> estimates the daily total from weight and a '
             'life-stage factor, but the veterinarian’s target takes priority. A calorie ceiling does not establish '
             'a safe shrimp dose or override a medical feeding plan. Compare <a href="/can-cats-eat/salmon/">cooked '
             'salmon</a> and <a href="/can-cats-eat/tuna/">tuna</a> as other optional seafoods with their own '
             'preparation concerns. There is no need to rotate through all of them to make a complete feline diet '
             'more complete.</p>'),
            ('After a swallowed tail or an unexplained reaction',
             '<p>Note whether shell, tail, packaging or a skewer may be missing, and describe any sauce. Gagging, '
             'trouble swallowing or abnormal breathing after eating requires urgent veterinary attention; do not try '
             'to push a suspected foreign object onward with more food. If the cat seems uncomfortable, contact the '
             'clinic rather than waiting for the next planned meal.</p><p>For digestive illness, <a '
             'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/vomiting">Cornell '
             'advises prompt evaluation when vomiting comes with weakness, lethargy, reduced appetite, blood or '
             'diarrhea</a>. Keep a record of the timing and amount without deciding that every reaction must be a '
             'seafood allergy. Your veterinarian can assess the possible causes and decide what to avoid next. Once '
             'a cat has reacted poorly to a particular food, continuing increasingly small taste tests is less '
             'useful than choosing a reward already known to suit its feeding plan.</p>')],
 'pumpkin': [('Start with the litter-box question, not the can',
              '<p>People often reach for pumpkin because a cat is straining, passing hard stool or having diarrhea. '
              'Those observations do not all describe the same problem. Before changing the food, establish what you '
              'have actually seen: urine, stool, repeated unsuccessful visits, vomiting or reduced appetite. A short '
              'dated note and a photograph of the output, where practical, can help the veterinarian understand the '
              'pattern.</p><p>Straining with little or no urine requires immediate veterinary attention. <a '
              'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feline-lower-urinary-tract-disease">Cornell\'s '
              'urinary-tract guidance</a> describes urethral obstruction as an emergency. Do not assume the cat is '
              'simply constipated and wait for pumpkin to work. This distinction is especially important when '
              'several cats share a litter box and you do not know which one produced the last normal clump. Ask for '
              'urgent advice if you cannot establish that a distressed cat is urinating.</p>'),
             ('Fiber is a tool selected for a case',
              '<p>Plain pumpkin contains fiber, but that fact alone cannot diagnose the reason for a stool change or '
              'identify the appropriate treatment. <a '
              'href="https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/disorders-of-the-stomach-and-intestines-in-cats">Merck\'s '
              'feline intestinal-disorder guidance</a> describes constipation management as more than adding a '
              'household ingredient; some cases need procedures and other medical care. A cat with an impacted colon '
              'is not made safe by continued spoonfuls of pumpkin.</p><p>A veterinarian may choose a dietary '
              'approach suited to that cat. Ask what food to use, how to measure the agreed amount, what result to '
              'expect and when to report back. Do not combine several fiber products just because each is described '
              'as natural. A complete therapeutic diet, a concentrated supplement and a can of pumpkin are different '
              'products. Copying one quantity across them can change the plan rather than simply improve '
              'compliance.</p>'),
             ('Read plain puree literally',
              '<p>Choose a product whose ingredients match the intended food. Plain canned pumpkin and pumpkin pie '
              'filling are not interchangeable, and a pumpkin-flavored drink is further removed again. Look at the '
              'complete label, not the orange color or seasonal name. If cooking fresh pumpkin for an optional '
              'taste, separate the flesh from hard skin and seeds, cook it without seasoning, cool it and mash a '
              'small amount.</p><p><a '
              'href="https://www.petpoisonhelpline.com/uncategorized/pet-friendly-human-food/">Pet Poison '
              "Helpline's produce guidance</a> includes pumpkin as an option for healthy pets; it does not endorse "
              'every pumpkin recipe as a treatment. Keep a separate plain portion before adding sugar, cream or '
              'seasonings for people. A pie, soup or coffee product may introduce ingredients addressed on the <a '
              'href="/can-cats-eat/milk/">milk</a>, <a href="/can-cats-eat/coffee/">coffee</a> or <a '
              'href="/can-cats-eat/onions/">onion</a> pages. If one is eaten accidentally, report the actual recipe '
              'instead of simply saying pumpkin.</p>'),
             ('A tiny taste and a prescribed addition have different aims',
              '<p>A healthy cat curious about plain puree may be offered a little as an optional extra if its '
              'feeding plan allows it. That is not the same as dosing pumpkin for a symptom. We do not publish a '
              'universal teaspoon-per-kilogram treatment schedule because the appropriate response depends on the '
              'clinical situation and product. More puree is not automatically a more effective '
              'intervention.</p><p>For energy planning, count an optional addition with other treats. The <a '
              'href="/cat-calorie-calculator/">calorie calculator</a> estimates the overall daily starting point; it '
              'cannot determine a fiber treatment amount. If a veterinarian recommends a regular addition, record '
              'the exact product and measure consistently. Do not replace a large share of the normal food with '
              'puree or use the empty space in the bowl as a guide. Our <a '
              'href="/guides/how-to-read-cat-food-labels/">label guide</a> helps keep complete nutrition separate '
              'from toppers and extras.</p>'),
             ('Decide in advance what means calling back',
              '<p>Ask the clinic for a follow-up point rather than repeating an ineffective home experiment '
              'indefinitely. Report worsening straining, repeated vomiting, pain, markedly reduced activity or poor '
              'eating promptly. <a '
              'href="https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats">Merck '
              'lists these as clinical warning signs</a>, not proof that a cat simply needs more fiber. Do not give '
              "human laxatives or enemas unless specifically directed for the cat; Merck's intestinal guidance warns "
              'that human laxatives may be dangerous for pets.</p><p>Keep track of stools, urine and the food '
              'actually eaten, including whether the cat rejected the pumpkin mixture and therefore ate less of its '
              'main diet. A food addition is not useful if it quietly disrupts intake. If the symptom resolves, ask '
              'whether the addition should continue rather than making it permanent by habit. For a different starch '
              'question, <a href="/can-cats-eat/rice/">the rice page</a> explains why a familiar bland-food '
              'reputation is also insufficient to choose a long-term feeding plan.</p>')],
 'blueberries': [('What the berry does, and what the marketing does not establish',
                  '<p>Blueberries sometimes arrive in cat-food discussions wearing a superfood label. That label can '
                  'distract from the modest decision in front of you: whether your particular cat enjoys a small '
                  'plain berry as an occasional reward. <a '
                  'href="https://vcahospitals.com/know-your-pet/using-food-and-treats-for-training-cats">VCA\'s '
                  'cat-treat guidance</a> includes blueberries among possible human-food treats. It does not '
                  'establish that giving berries prevents feline cancer, improves eyesight or replaces a therapeutic '
                  'diet. We make none of those promises.</p><p>A blueberry on an ingredient list is also different '
                  'from blueberries served by the handful. Manufacturers formulate complete diets from combinations '
                  'of ingredients; a household bowl of fruit is not a formulation. The <a '
                  'href="/guides/how-to-read-cat-food-labels/">label-reading guide</a> helps distinguish a '
                  'nutritional-adequacy statement from decorative pictures on a packet. Choose the everyday food on '
                  'that basis, and decide about berry treats separately.</p>'),
                 ('Make a rolling berry easy to supervise',
                  '<p>A round fruit can disappear under furniture or be swallowed quickly while another cat is '
                  'approaching. Wash a fresh berry, check it for visible spoilage and split or flatten a small part '
                  'onto a dish. Put the dish where you can see the cat take it, away from a busy feeding '
                  'competition. Do not throw berries around as if they were dry toy balls; food rolling out of sight '
                  'is harder to retrieve and harder to include in a feeding record.</p><p>Frozen blueberries should '
                  'be allowed to soften rather than offered as hard frozen objects. These are conservative household '
                  'preparation choices, not measurements of a known choking rate. Stop if your cat struggles with '
                  'the texture. A cat that sniffs and walks away has given a useful answer: use a reward it already '
                  'understands, or try play and attention rather than insisting on the fruit.</p>'),
                 ('Follow the other ingredients through the kitchen',
                  '<p>A blueberry muffin, a spoonful of yogurt and a sweetened berry syrup are three different '
                  'products. Read each one instead of borrowing the plain-fruit verdict. Chocolate chips matter even '
                  'if the muffin looks mostly blue; see the <a href="/can-cats-eat/chocolate/">chocolate page</a>. '
                  'Dairy mixtures raise the questions explained on our <a href="/can-cats-eat/yogurt/">yogurt '
                  'page</a>, including whether the cat tolerates dairy and whether the product is plain.</p><p>The '
                  '<a '
                  'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
                  'food-hazard list</a> is useful for checking harmful additions, but a familiar fruit name on the '
                  'front is not a substitute for the back label. Keep mixed desserts out of reach while baking or '
                  'clearing plates. If a cat steals part of one, save the wrapper and recipe, estimate the missing '
                  'amount and speak to a veterinarian about the actual mixture. Reporting only that it ate '
                  'blueberries omits information the clinic may need.</p>'),
                 ('Keep rewards useful without making a fruit ration',
                  '<p>Before a training session, choose what behavior you are rewarding and divide the chosen food '
                  'into tiny usable pieces. You need a reward the cat values, not a large serving. If the cat works '
                  'happily for part of its normal ration, that may avoid adding a new food at all. Blueberries have '
                  'no special status that requires you to continue after the cat loses interest.</p><p>Include the '
                  'fruit with all other extras in the day. Our <a href="/cat-calorie-calculator/">calorie '
                  'calculator</a> estimates the overall energy starting point; it does not assess the safety of an '
                  'ingredient or supply the energy density of your berries. Do not subtract a meal just because the '
                  'cat had an unmeasured berry snack. If rewards are frequent enough to affect normal intake, ask '
                  'the clinic to help set a practical daily allowance and use a reproducible measure.</p>'),
                 ('Trouble after a berry trial needs a clear history',
                  '<p>Introduce only one unfamiliar snack at a time so there is a useful record if something '
                  'changes. Note whether the berries were fresh, thawed or part of a prepared product. Stop the '
                  'experiment if the cat vomits or develops diarrhea. <a '
                  'href="https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats">Merck\'s '
                  'digestive overview</a> lists these symptoms among signs with many possible causes; timing alone '
                  'cannot prove the berry was responsible. Repeated symptoms, blood, pain or reduced appetite '
                  'deserve veterinary advice.</p><p>For a cat on an elimination diet, even an apparently simple '
                  'treat can complicate the agreed feeding plan. Ask before adding it, and record any accidental '
                  'extras. If you would rather compare another fruit, read the distinct preparation and product '
                  'cautions for <a href="/can-cats-eat/strawberries/">strawberries</a>. There is no need to rotate '
                  'through a fruit menu. A predictable, adequate main diet matters more than producing a colorful '
                  'snack bowl.</p>')],
 'watermelon': [('Water in fruit is not a hydration treatment',
                 '<p>Watermelon is often described as a hydrating snack, which can be misunderstood as advice for a '
                 'cat that is drinking poorly. Those are different situations. A healthy cat may investigate a '
                 'little prepared flesh; a cat that might be dehydrated needs an appropriate assessment, not a bowl '
                 'of melon. The <a '
                 'href="https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/feeding-your-cat">Cornell '
                 'feeding guide</a> emphasizes access to fresh water. Keep normal water sources available regardless '
                 'of whether a fruit taste is offered.</p><p>Do not interpret refusal of watermelon as evidence that '
                 'a cat is failing to drink enough. Equally, eating melon does not demonstrate that hydration is '
                 'adequate. Our <a href="/guides/senior-cat-weight-and-appetite/">senior weight and appetite '
                 'guide</a> is a more useful starting point when drinking, eating or weight has changed. Describe '
                 'those changes to the clinic, particularly if the cat seems unwell or is urinating '
                 'differently.</p>'),
                ('Start with a clean cutting board and finish without the rind',
                 '<p>Use the flesh from a freshly cut piece, removing the rind and any seeds you find, including in '
                 'a melon sold as seedless. Our conservative preference is a soft, small piece on a dish rather than '
                 'a large slippery cube held at face height. Discard rind before letting a curious cat investigate '
                 'the cutting area. Do not let it chew the green shell because a person has scraped out most of the '
                 'pink part.</p><p><a '
                 'href="https://vcahospitals.com/know-your-pet/using-food-and-treats-for-training-cats">VCA includes '
                 'seedless watermelon in its cat-treat examples</a>. That is support for a plain, limited option, '
                 'not a guarantee about all parts of the fruit or any portion size. Rind and seeds are not necessary '
                 'to offer a taste, so removing them avoids an unnecessary uncertainty. You do not need a claim that '
                 'every swallowed seed poisons cats to make that sensible preparation choice.</p>'),
                ('Fruit salad changes the question',
                 '<p>Check the entire bowl before sharing from it. A watermelon cube touching an unknown syrup or '
                 'mixed with other fruit is not as straightforward as flesh cut separately. Grapes and raisins are '
                 'foods we advise avoiding because feline evidence is limited and professional advice is appropriate '
                 'after ingestion; see <a href="/can-cats-eat/grapes/">the grape page</a>. Do not assume a mixed '
                 'bowl is acceptable because the biggest pieces are watermelon.</p><p>The same attention applies to '
                 'slush drinks, cocktails, fruit pops and desserts. Alcohol is a separate hazard described by <a '
                 'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA</a> '
                 'and on our <a href="/can-cats-eat/alcohol/">alcohol page</a>. Neither freezing nor fruit flavor '
                 "removes it. Keep a cat away from drink preparation and discarded cups, and report the drink's "
                 'ingredients if one is licked. A photograph of the label is more informative than the general word '
                 'watermelon.</p>'),
                ('A calorie example has limits',
                 '<p>Use the <a href="/cat-calorie-calculator/">calorie calculator</a> to see how body weight and '
                 "life-stage selection interact. For a 4 kg cat, RER is about 198 kcal per day; the site's "
                 'neutered-adult multiplier of 1.2 gives about 238 kcal. Under a ten-percent treat ceiling, all '
                 'extras together would fit below roughly 24 kcal. That ceiling includes rewards and any food used '
                 'with medicine, not just fruit.</p><p>This arithmetic does not establish a clinically safe melon '
                 "weight or make the estimate correct for every 4 kg cat. The cat's real energy needs and medical "
                 'diet can differ. If measuring regular treats, use a reliable value for the actual food and weigh '
                 'the edible portion. Avoid converting an unmeasured cube using a guessed size. A small optional '
                 'taste is enough for a cat that likes it; no melon allowance needs to be filled.</p><p>The '
                 'exponential RER formula and neutered-adult factor used here are described in <a '
                 'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck\'s '
                 'energy reference</a>; <a '
                 'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA '
                 'supports the ten-percent treat ceiling</a>, rather than these particular rounded daily '
                 'estimates.</p>'),
                ('Watch swallowing, then the normal routine',
                 '<p>Stay nearby while the cat tries a new texture. Difficulty breathing, persistent gagging or an '
                 'inability to swallow needs urgent attention, especially if rind or another object may have been '
                 'taken. Do not push additional food or water into a cat that is struggling. Tell the clinic exactly '
                 'what part of the fruit is missing and when the episode started.</p><p>Later vomiting, loose stool '
                 'or loss of appetite should end the snack trial. <a '
                 'href="https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats">Merck '
                 'describes digestive signs</a> that may need investigation rather than a home diagnosis based on '
                 'the last ingredient offered. Keep track of whether the cat eats its usual food and behaves '
                 'normally. For an uncomplicated future comparison, <a '
                 'href="/can-cats-eat/cantaloupe/">cantaloupe</a> has its own preparation notes. Neither melon needs '
                 'to be added to the diet of a cat that prefers its regular food.</p>')],
 'strawberries': [('A plain berry is the starting point',
                   '<p>For a cat interested in strawberries, assess an ordinary fresh berry before thinking about '
                   'desserts or nutritional claims. <a '
                   'href="https://vcahospitals.com/know-your-pet/using-food-and-treats-for-training-cats">VCA lists '
                   'strawberries as a possible cat treat</a>. That supports an occasional plain option; it does not '
                   'provide a feline treatment dose or show that strawberry snacks improve immunity. There is no '
                   'need to persuade a disinterested cat to eat them.</p><p>Wash the berry, remove the leafy top and '
                   'cut a very small portion of the flesh onto a clean dish. Removing the top is a simple '
                   "preparation choice, not a claim that ordinary strawberry leaves have the apple seed's toxic "
                   'mechanism. Do not transfer warnings from <a href="/can-cats-eat/apples/">apple plant parts</a> '
                   'to every fruit. Different fruits have different issues, and an accurate explanation is more '
                   'useful than labeling all seeds, leaves and skins identically dangerous.</p>'),
                  ('The vitamin-C assumption misses feline biology',
                   '<p>Advertising for berries often emphasizes vitamin C. A reason to choose a food for people is '
                   "not automatically a reason to add it to a cat's bowl. <a "
                   'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck\'s '
                   'nutritional reference</a> explains that cats can synthesize vitamin C and do not have an AAFCO '
                   'dietary requirement for it. A strawberry therefore is not a necessary way to prevent a missing '
                   'dietary vitamin in a cat eating an appropriate complete food.</p><p>This also does not mean '
                   'fruit has no calories or that every supplement is harmless. Think about what problem you are '
                   'trying to solve. If the answer is simply that the cat wants to investigate your snack, a limited '
                   'taste or a non-food interaction can satisfy the situation. If the answer is a health concern, '
                   'bring it to the veterinarian. Food interest cannot tell you that a vitamin deficiency '
                   'exists.</p>'),
                  ('Chocolate coating and dairy turn it into a different food',
                   '<p>The bright red fruit inside a dessert is often the least useful part of its name. A '
                   'chocolate-covered strawberry is a <a href="/can-cats-eat/chocolate/">chocolate exposure</a>, and '
                   'a berry milkshake is a dairy mixture. The <a '
                   'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
                   "hazard list</a> describes chocolate's methylxanthines and warns that dairy may upset pets' "
                   'digestion. Do not scrape a coating off and assume nothing remains on the fruit. Reserve a '
                   'separate plain berry before preparing dessert instead.</p><p>Check jams, syrups, cheesecake '
                   'toppings and flavored yogurt independently. Ingredients and concentrations vary by product. If a '
                   'cat stole part of a sweetened or sugar-free mixture, retain the actual label; do not report only '
                   'strawberry flavor. For dairy-specific questions, read <a href="/can-cats-eat/yogurt/">our yogurt '
                   'page</a>. The ingredient check is particularly important when you did not make the food yourself '
                   'and cannot see how it was prepared.</p>'),
                  ('Choose a portion you can account for',
                   '<p>A small taste is easier to fit into the day than fruit offered throughout an afternoon. Put '
                   'the chosen portion on one dish and clear it away afterward, so another member of the household '
                   'does not assume the cat has had none. A treat jar or written list can be useful when different '
                   'people give rewards, even if each person believes their own contribution is tiny.</p><p>The <a '
                   'href="/cat-calorie-calculator/">calorie calculator</a> provides a starting daily energy '
                   "estimate. Compare it with your clinic's advice and include all extras together. <a "
                   'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA\'s '
                   'feline treat sheet</a> recommends keeping treats within ten percent of total daily calories. '
                   'That is an upper limit for the category, not a strawberry target. Size descriptions are '
                   'imprecise, so a repeated measured serving needs a real food-energy value rather than a guessed '
                   'calorie count attached to the words one berry.</p>'),
                  ('If the cat feels unwell, stop experimenting',
                   '<p>Offer a first taste when the cat is otherwise well, rather than during an unexplained stomach '
                   'problem. A simple note of the time and amount helps if symptoms follow. Vomiting or diarrhea '
                   'should end the trial; do not follow it immediately with blueberries to find a better fruit. <a '
                   'href="https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats">Merck\'s '
                   'digestive overview</a> describes such signs as reasons to consider the broader clinical history, '
                   'rather than proof of a single food allergy.</p><p>Seek prompt veterinary advice for repeated '
                   'symptoms, pain, blood, unusual quietness or reduced eating, and urgent care for breathing '
                   'difficulty or collapse. If the cat ate a dessert, tell the clinic about every ingredient you can '
                   'establish. A healthy cat that ignores the prepared flesh can simply return to its normal meal. '
                   'The optional berry should not become a contest that disrupts a reliable feeding routine.</p>')],
 'cantaloupe': [('Curiosity about melon does not diagnose a craving',
                 '<p>A cat sniffing cantaloupe has shown interest in the object in front of it, not demonstrated a '
                 'nutritional deficiency. There is no need to assign a medical meaning to that interest or claim '
                 "that the melon smells like meat to every cat. A veterinarian's <a "
                 'href="https://www.petco.com/pet-education/cat/vet-qa/cat-eat-cantaloupe-safety">cantaloupe answer '
                 'published by Petco</a> supports occasional small amounts and cautions that larger servings may '
                 'cause digestive upset. That is a more modest conclusion than calling cantaloupe an essential '
                 "feline superfood.</p><p>Decide first whether an extra food fits your cat's current plan. If it "
                 'does, prepare a small taste of clean flesh. If your cat has a prescribed diet or there is already '
                 'an unexplained appetite problem, leave the melon aside until you have advice. The goal is an '
                 'uncomplicated optional experience, not a new ingredient that makes an existing medical question '
                 'harder to evaluate.</p>'),
                ('Prepare the melon before inviting the cat over',
                 '<p>Wash the outside before cutting, use a clean board and separate a piece of edible flesh from '
                 'the rind and seed cavity. This sequence keeps the cat away from the knife, discarded parts and a '
                 'tempting half melon on the counter. Put scraps away promptly. Even a household that never '
                 'deliberately feeds rind can have an accidental exposure when the bin is left open.</p><p>Our '
                 'conservative serving suggestion is a soft, small piece of flesh on a dish, without rind or seeds. '
                 'It is not a trial-derived safe dose. Do not let the cat chew a broad rind strip as a play object '
                 'or swallow a large slick cube because it is technically soft. A cat that struggles with a texture '
                 'should not be encouraged to continue. Compare the distinct preparation advice for <a '
                 'href="/can-cats-eat/watermelon/">watermelon</a> if that is the fruit you actually have.</p>'),
                ('Keep a fruit cup separate from a plain melon',
                 '<p>Read mixed fruit bowls as complete recipes. Some include grapes, a syrup or a topping; canned '
                 'or packaged products may not match what the picture suggests. The advice for <a '
                 'href="/can-cats-eat/grapes/">grapes</a> should guide a grape-containing exposure, even if most of '
                 'the portion appears to be cantaloupe. Removing one visible ingredient after the cat has eaten does '
                 'not tell the clinic what was swallowed.</p><p>Similarly, a melon-flavored drink or frozen dessert '
                 'is not just chopped fruit. Alcohol and dairy mixtures raise separate questions covered in <a '
                 'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA\'s '
                 "people-foods guidance</a>. Reserve the cat's possible taste before making a cocktail, smoothie or "
                 'dressed fruit salad. If the ingredient list is unknown, there is no need to take a chance for a '
                 'snack the cat does not require. Keep the packaging if an accidental taste has already '
                 'happened.</p>'),
                ('Let the normal diet carry the nutritional job',
                 '<p>Complete cat food and a small fruit extra have different roles. The <a '
                 'href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11107985/">2022 ISFM nutrition guidance</a> '
                 'explains feline requirements for nutrients such as taurine and preformed vitamin A. A colorful '
                 'piece of melon does not reproduce that balance. Do not reduce the main diet by a bowl-sized amount '
                 'just to make a fruit serving look intentional, and do not use cantaloupe as the basis of a '
                 'homemade diet.</p><p>Our <a href="/guides/how-to-read-cat-food-labels/">food-label guide</a> shows '
                 'how to check whether the everyday food is intended as complete nutrition. The <a '
                 'href="/cat-calorie-calculator/">calorie calculator</a> helps with energy planning, but neither '
                 'tool prescribes a melon portion. Count any taste with other extras and avoid repeatedly topping up '
                 'the dish. A cat can enjoy an interaction with you without having a different ingredient added to '
                 'every meal.</p>'),
                ('When the apparent melon problem needs a clinic',
                 '<p>After an accidental mouthful, work out whether it was flesh, rind, seeds or a mixed product. '
                 'Tell the veterinarian approximately how much is missing and when it happened. Keep an eye on the '
                 "cat's ability to swallow, normal activity and subsequent appetite. Breathing difficulty, "
                 'persistent gagging or collapse warrants urgent care, particularly when a piece of rind or another '
                 'object could be involved.</p><p>Repeated vomiting, diarrhea or abdominal discomfort is a reason to '
                 'stop optional foods and obtain veterinary advice. <a '
                 'href="https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats">Merck '
                 'lists these digestive signs</a> within a broader range of possible disorders. Do not assume the '
                 'melon alone explains every symptom or keep trying different fruits to settle the stomach. If the '
                 'cat is well but uninterested, remove the uneaten portion and continue the established feeding '
                 'routine. That is a perfectly acceptable outcome for an optional snack.</p>')],
 'carrots': [('The vitamin-A story changes when the eater is a cat',
              '<p>Carrots are famous for their association with vitamin A, but feline biology makes the popular '
              'human-food slogan misleading here. <a '
              'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck\'s '
              'nutritional reference</a> explains that cats cannot convert beta-carotene into the vitamin A they '
              'require and need a preformed dietary source. A cooked carrot bite therefore is not a remedy for '
              'suspected vitamin-A deficiency or poor vision.</p><p>The useful role of a carrot, if your cat enjoys '
              'one, is much smaller: an optional plain snack with a texture you can control. Do not replace part of '
              'a complete feline diet with a growing vegetable portion because the color looks nutritious. If there '
              'is an eye problem, a veterinary examination is the next step, not more carrots or an unprescribed '
              'vitamin supplement. Our <a href="/guides/how-to-read-cat-food-labels/">label-reading guide</a> helps '
              'identify an appropriate everyday diet without turning a single ingredient into a cure.</p>'),
             ('Soft pieces are a more practical choice than a hard stick',
              '<p>For household sharing, steam or boil a little carrot in plain water until soft, let it cool and '
              'separate a small amount into manageable pieces. There is no need to offer a long raw stick for the '
              'cat to chew. <a href="https://www.rspca.org.uk/adviceandwelfare/seasonal/christmas">RSPCA\'s seasonal '
              'food advice</a> specifically distinguishes preparation for cats and recommends small pieces or '
              'cooking until soft to reduce choking concerns.</p><p>This is about making eating easier to supervise, '
              'not claiming that every raw carrot is poisonous. If your cat gulps food, has dental problems or '
              'struggles with pieces, the best choice may be to avoid this snack entirely. Do not force a vegetable '
              'into its mouth to test whether it can chew. Keep the raw peelings and large chunks off the floor '
              'while you prepare dinner, especially if the cat is following the chopping board.</p>'),
             ('A plain reserve prevents a seasoning puzzle',
              "<p>Set aside the cat's possible taste before glazing or seasoning the pan. Roasted carrots with "
              'onion, garlic butter, stock powder or a packaged soup mix are different dishes. <a '
              'href="https://www.aspca.org/news/pets-and-produce-top-tips-vegetable-garden-safety">ASPCA\'s produce '
              'guidance</a> identifies Alliums as a red-blood-cell hazard in cats and includes plain carrots among '
              'moderate snack options. The vegetable does not make its sauce harmless.</p><p>Honey glaze, cream and '
              'dessert mixtures add unnecessary variables even where no specific toxin is present. Instead of trying '
              'to rinse a finished dish and guessing how much seasoning remains, use a separately prepared piece. '
              'For an accidental exposure, save the recipe and list any stock cube, sauce or seasoning blend. The <a '
              'href="/can-cats-eat/onions/">onion page</a> and <a href="/can-cats-eat/garlic/">garlic page</a> '
              'explain why powder forms matter. A report that the cat ate carrots alone would hide the part most '
              'relevant to assessment.</p>'),
             ('Do not turn a treat into an improvised weight-loss diet',
              '<p>Replacing a large share of food with carrots is a different intervention from offering a taste. It '
              'changes what the cat eats across the day and can crowd out the main diet. A weight-management plan '
              'needs a useful calorie target and a nutritionally appropriate food, rather than a rule to bulk out '
              'the bowl with whichever vegetables are in the fridge.</p><p>Use the <a '
              'href="/cat-calorie-calculator/">calorie calculator</a> as a discussion starting point, then agree the '
              'feeding amount with your veterinary team. It cannot assess body condition or decide whether carrot is '
              'suitable for a cat\'s medical history. Compare <a href="/can-cats-eat/green-beans/">green beans</a> '
              'for another optional vegetable, but do not assume combining low-calorie ingredients makes a balanced '
              'ration. If training rewards are needed often, portions from an agreed main ration are easier to '
              'account for than an ever-changing bowl of scraps.</p>'),
             ('Know when to stop the experiment',
              '<p>Supervise the first taste and put the rest away. If the cat coughs, gags, paws at its mouth or '
              'seems unable to swallow, stop feeding and seek advice; breathing difficulty is an emergency. Report '
              'whether the piece was raw or cooked and its approximate size. Do not try to push another food down to '
              'move a suspected obstruction.</p><p>Afterward, note any vomiting, diarrhea, reduced appetite or '
              'apparent pain. <a '
              'href="https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats">Merck\'s '
              'digestive overview</a> explains that these are clinical signs rather than diagnoses. Persistent or '
              'repeated changes need veterinary attention, not a switch from carrots to pumpkin as a home remedy. '
              'Keep the history simple: the preparation, quantity, timing and every other food offered. If the cat '
              'is comfortable and rejects the carrot, no replacement vegetable is required. Continue the reliable '
              'everyday feeding routine and use a different kind of reward.</p>')],
 'green-beans': [('A bean does not make a complete weight-management diet',
                  '<p>The most consequential green-bean mistake is not a single plain taste. It is replacing a '
                  "substantial amount of the cat's usual food with beans in an attempt to create a do-it-yourself "
                  'weight-loss diet. That changes the balance of the whole ration, not just its size. The <a '
                  'href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11107985/">ISFM nutritional guidance</a> explains '
                  'that feline requirements extend beyond simply filling the stomach. A bowl can look generous while '
                  'supplying too little of the food intended to meet those requirements.</p><p>If weight is the '
                  'concern, record the existing food, measured portions, treats and recent scale readings. Take that '
                  'information to the veterinary team before making a major replacement. Our <a '
                  'href="/cat-calorie-calculator/">calorie calculator</a> can provide a starting estimate, but it '
                  'does not assess muscle, body condition or the nutritional adequacy of a bean-based ration. Do not '
                  'interpret a lower calorie count as proof that the new ration is appropriate.</p>'),
                 ('Choose the bean you actually mean',
                  '<p>This page is about ordinary green beans served plainly, not every food with bean in its name. '
                  'A bag of frozen green beans, a can in salted liquid and a ready-made casserole are different '
                  'products. <a href="https://www.petpoisonhelpline.com/uncategorized/pet-friendly-human-food/">Pet '
                  "Poison Helpline's produce guidance</a> includes green beans among optional snacks for healthy "
                  'pets. That should not be stretched into a claim that every legume, raw dried bean or prepared '
                  'bean dish has been assessed here.</p><p>For a manageable kitchen option, steam or boil plain '
                  'green beans until tender, let them cool, trim them and chop a small amount. These are '
                  'conservative preparation choices rather than a validated dose or a treatment protocol. If using '
                  "packaged beans, check the ingredients before opening the cat's dish. Keeping a separate plain "
                  'portion is simpler than trying to pick acceptable pieces out of a finished meal.</p>'),
                 ('Casserole brings the ingredients the name leaves out',
                  '<p>A green-bean casserole can include fried onion, garlic, stock, cream and toppings. The '
                  'important question is not whether a green bean itself appears on an acceptable-food list. It is '
                  'whether the particular dish contains something harmful. <a '
                  'href="https://www.aspca.org/news/pets-and-produce-top-tips-vegetable-garden-safety">ASPCA '
                  'identifies Alliums as a concern for cats</a>; our <a href="/can-cats-eat/onions/">onion page</a> '
                  'explains the different fresh, cooked and powdered forms.</p><p>Do not assume rinsing a sauced '
                  'bean establishes that the seasoning has gone. You cannot measure that by looking. Set aside a '
                  'separate plain portion before cooking the household meal, or choose not to share. If an '
                  'accidental mouthful occurred, retain the sauce label or recipe and include it in the veterinary '
                  "history. A can's liquid and a restaurant dressing are part of the exposure even when the solid "
                  'pieces are easy to recognize.</p>'),
                 ('A useful reward is one the cat wants',
                  '<p>Some cats will investigate a small tender bean piece, while others will ignore it. Do not keep '
                  'escalating portion size to make an uninterested cat participate. A food reward only works if the '
                  'cat values it, and training can also use a familiar piece from the normal ration or a favorite '
                  'interaction. Offer a little separately so you can see whether it is eaten, rather than scattering '
                  'chopped beans among the main food and making that meal less predictable.</p><p>Count any '
                  'swallowed portion with other extras. <a '
                  'href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA\'s '
                  'feline treat sheet</a> gives a ten-percent ceiling for treats, not a required vegetable quota. If '
                  'you want to compare another food, the <a href="/can-cats-eat/peas/">pea page</a> distinguishes a '
                  'formulated ingredient from a home addition. Neither food becomes unlimited simply because it is '
                  'green, inexpensive or convenient to keep in the freezer.</p>'),
                 ('When beans are a distraction from the real problem',
                  '<p>Do not start a bean experiment when the cat has unexplained vomiting, loose stool, '
                  'constipation or appetite changes. First preserve the normal feeding history and ask the clinic '
                  'what needs investigating. For example, <a '
                  'href="https://vcahospitals.com/know-your-pet/diarrhea-in-cats">VCA\'s feline diarrhea '
                  'guidance</a> explains why a symptom can have several causes and why treatment depends on the '
                  'case. Adding different vegetables every day can make the timing harder to understand.</p><p>If a '
                  'new snack is followed by symptoms, stop it and note the preparation, quantity and time. Contact '
                  'the clinic for repeated symptoms or a cat that is painful, unusually quiet or eating less. '
                  'Breathing or swallowing difficulty needs urgent attention. Keep track of whether a long bean, a '
                  'piece of packaging or part of a mixed dish is missing. A concise description of the actual food '
                  'helps more than concluding that green beans must be either universally safe or universally '
                  'harmful.</p>')],
 'peas': [('An ingredient in a formulated food is not a home recipe',
           '<p>Seeing peas on a cat-food label does not tell you how many spoonfuls to add at home. Commercial '
           'recipes combine ingredients to achieve a nutritional profile; a household addition changes a finished '
           'ration without automatically maintaining that balance. The <a '
           'href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11107985/">ISFM feline nutrition guidance</a> describes '
           'requirements that cannot be judged from a single ingredient. It also makes clear that cats can use '
           'suitably processed starch even though it is not an essential dietary requirement.</p><p>That is why two '
           'sweeping claims are unhelpful: peas are in cat food so they must be necessary as a snack, or cats are '
           'carnivores so any pea ingredient proves a food is unsuitable. Use the <a '
           'href="/guides/how-to-read-cat-food-labels/">label guide</a> to assess the stated purpose of the entire '
           'product. Treat a few household peas as a separate optional choice, not a correction to a supposedly '
           'incomplete ingredient list.</p>'),
          ('Plain garden peas, prepared so you can see them eaten',
           '<p>The <a href="https://www.aspca.org/news/pets-and-produce-top-tips-vegetable-garden-safety">ASPCA '
           'produce article</a> includes peas among garden foods that may be offered in moderation. For a simple '
           'household option, choose plain garden peas, cook or fully thaw them as appropriate to the product and '
           'let any hot portion cool. Mash or split a small amount on a dish. This makes a round rolling item easier '
           'to supervise without pretending that there is a scientifically established number of peas that suits '
           'every cat.</p><p>Do not offer a hard frozen handful or assume that the cat must enjoy chasing peas '
           'around the kitchen. Keep the first attempt quiet and small. Discard tough pods or packaging rather than '
           'leaving them as play objects near the bowl. If the cat ignores the prepared food, it does not need to '
           'learn to like it. An already familiar reward can make the interaction simpler.</p>'),
          ('The casserole and soup are not the same snack',
           '<p>Peas cooked in plain water are easy to identify. Pea soup, a creamy side dish, mint sauce, fried rice '
           'and onion gravy require ingredient-by-ingredient assessment. Read labels for <a '
           'href="/can-cats-eat/onions/">onion</a> or <a href="/can-cats-eat/garlic/">garlic</a>, including powders. '
           "ASPCA's produce guidance explains the Allium concern; being mixed with vegetables does not remove "
           'it.</p><p>Even where no specific toxic ingredient is identified, a rich mixed dish is an unnecessary way '
           'to offer a pea taste. Reserve a little separately before seasoning instead of trying to pick peas clean '
           'with a fork. If a cat stole a prepared dish, save the recipe and packaging. Tell the clinic whether it '
           'was a plain pea, a sauce lick or an entire mouthful. The amount and full recipe matter more than the '
           "main ingredient's name.</p>"),
          ('Do not build a protein or grain-free argument around one pea',
           '<p>A pea is not interchangeable with a complete feline food or a portion of meat merely because both '
           "contain nutrients. Likewise, a food's grain-free wording does not by itself establish whether its full "
           "formula is suitable. Keep attention on what the product is designed to provide and on the cat's actual "
           'needs. Avoid trying to compensate for one ingredient by adding extra peas, rice or chicken from the '
           'kitchen.</p><p>If the everyday diet needs review, bring the exact package, feeding amount and reason for '
           'concern to the veterinary team. Use the <a href="/cat-calorie-calculator/">calorie calculator</a> to '
           'organize an energy question, not as proof of nutritional completeness. It can estimate kcal without '
           'knowing whether a meal meets amino-acid or mineral requirements. The <a href="/can-cats-eat/rice/">rice '
           'page</a> explains the same distinction for another common cooked ingredient in a different household '
           'setting.</p>'),
          ('Keep optional trials out of an active medical work-up',
           '<p><a href="https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-cat-v2.pdf">WSAVA '
           'advises checking treat suitability</a> for cats with medical conditions, dietary sensitivities or '
           'prescribed diets. A cat undergoing an elimination trial should not receive peas just because they look '
           'plain. Ask whether they fit the agreed plan and record any accidental extras. With more than one cat in '
           'the home, use a separate supervised dish so you know which animal actually ate the snack.</p><p>If '
           'vomiting or loose stool follows, stop the trial and write down the timing rather than declaring a new '
           'allergy from one episode. Persistent symptoms, pain or loss of normal appetite need veterinary advice. '
           '<a href="https://vcahospitals.com/know-your-pet/diarrhea-in-cats">VCA\'s diarrhea guidance</a> discusses '
           'the range of possible causes. Difficulty breathing or swallowing is urgent. Do not respond by adding '
           'pumpkin, another vegetable or a human medicine before seeking advice. A stable, well-described feeding '
           'history is more useful than a sequence of improvised remedies.</p>')],
 'rice': [('Edible starch is not a complete feline meal',
           '<p>Plain cooked rice is not the same thing as a rice-based feeding plan. The <a '
           'href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11107985/">2022 ISFM feline nutrition guidance</a> '
           'explains that cats can digest and use appropriately processed starch, while still having requirements '
           'that starch cannot meet by itself. Calling cats carnivores does not mean every cooked grain is '
           'poisonous. Calling rice digestible does not mean it can replace a balanced diet.</p><p>If a healthy cat '
           'steals a few grains from a plate, identify whether they were truly plain before deciding what the '
           'exposure involved. A substantial portion of rice served repeatedly is a different concern because of '
           'what it may displace. Our <a href="/guides/how-to-read-cat-food-labels/">food-label guide</a> helps '
           'distinguish a complete product from a complementary food. A bowl of white rice remains an ingredient '
           'even when it is soft, familiar and easy to serve.</p>'),
          ('Why the chicken-and-rice shortcut needs a second look',
           '<p>Rice is commonly mentioned when a cat has diarrhea, but the familiar name of a home recipe does not '
           'identify the cause or the right diet. <a '
           'href="https://vcahospitals.com/know-your-pet/bland-diet-instructions-for-dogs-and-cats">VCA\'s guidance '
           'on bland diets</a> explains that chicken and rice is nutritionally incomplete and that more appropriate '
           'formulated gastrointestinal diets are available. This is why we do not publish a universal '
           'chicken-to-rice ratio or instruct owners to keep a sick cat on it indefinitely.</p><p>If your '
           'veterinarian says to use a bland diet, ask which exact food, what measured daily amount and for how '
           'long. The word bland can describe very different feeding intentions. Keep track of what the cat actually '
           'eats, rather than assuming a full-looking bowl means its needs were met. If it rejects the agreed food, '
           'report that promptly instead of silently replacing it with rice alone or a succession of human '
           'leftovers.</p>'),
          ('Plain cooking means no stock cube',
           '<p>For an optional taste, use well-cooked rice prepared in plain water and cooled to a comfortable '
           'temperature. Do not count a broth-cooked pot as plain without checking the broth. Stock, onion powder '
           'and garlic can be easy to overlook because the finished grains do not look seasoned. <a '
           'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA '
           'identifies onion and garlic among foods to avoid</a>; our <a href="/can-cats-eat/garlic/">garlic '
           'page</a> explains why small-looking powder additions matter.</p><p>Fried rice, risotto, pilaf, rice '
           'pudding and sushi are separate dishes with their own ingredients. Scraping off a visible topping cannot '
           'reconstruct a plain portion. If you want to reserve some, do so before sauces or additions enter the '
           'pan. Uncooked dry rice is not the preparation discussed here and offers no advantage as a snack. Keep '
           'dry goods and opened packets away from a cat that chews packaging.</p>'),
          ('Measure the cooked food, not an imagined serving',
           '<p>Rice absorbs water during cooking, so a spoon of dry grains and a spoon of cooked rice are not '
           'interchangeable measures for energy planning. If a veterinarian has specified a weighed addition, '
           'clarify whether the weight refers to cooked or uncooked product and follow that instruction '
           'consistently. Do not use a generic cup description to decide how much normal cat food to '
           'remove.</p><p>The <a href="/cat-calorie-calculator/">calorie calculator</a> estimates overall daily '
           'energy from body weight and a selected factor. It cannot supply the energy density of your pot or '
           'confirm nutritional adequacy. An optional rice taste belongs with other extras, not in a separate '
           'unrestricted category. If the cat has a medical feeding plan, ask whether any rice fits it before '
           'offering it. The <a href="/can-cats-eat/oatmeal/">oatmeal page</a> makes a similar distinction for '
           'another cooked grain whose preparation changes the weight and texture substantially.</p>'),
          ('Use symptoms to seek help, not to choose the next home remedy',
           '<p>Repeated vomiting, blood in stool, marked lethargy, pain or poor eating are reasons to contact a '
           'veterinarian rather than simply increasing rice. <a '
           'href="https://vcahospitals.com/know-your-pet/diarrhea-in-cats">VCA\'s feline diarrhea information</a> '
           'describes diarrhea as a sign with multiple possible causes. A normal-looking stool after a home meal '
           'also does not prove that a suspected toxin, foreign object or underlying disease has been dealt '
           'with.</p><p>Save the recipe or packaging after an accidental meal and tell the clinic about raw '
           'ingredients, sauce and any non-food material that could have been swallowed. Keep the history brief but '
           'complete: what was eaten, approximately how much, when, and what changed afterward. Do not add human '
           'anti-diarrhea medicine or begin prolonged fasting on the basis of an online rice suggestion. The feeding '
           "instructions should match the cat's age, condition and actual assessment, not the reputation of a "
           'kitchen staple.</p>')],
 'oatmeal': [('A bowl for a cat is different from your breakfast',
              '<p>Oatmeal can mean plain oats cooked in water or a large breakfast assembled from milk, dried fruit, '
              "syrup and flavorings. Those are not equivalent exposures. Purina's nutrition article <a "
              'href="https://www.purina.com/articles/cat/feeding/can-cats-eat/oatmeal">discusses plain oatmeal as an '
              'occasional small treat</a>, but it does not make a finished human breakfast a balanced meal for a '
              'cat. Keep the question narrow: a small amount of plainly cooked oats, if that fits the individual '
              "cat's diet.</p><p>There is no requirement to introduce cereal merely because someone else reports "
              'that their cat likes it. If your cat already eats an appropriate complete food and is comfortable '
              'with its feeding routine, a new breakfast ingredient is optional. An unusual appetite, repeated food '
              'refusal or a change in weight should prompt a review of the overall situation, not a plan to replace '
              'the usual meal with oatmeal.</p>'),
             ('Cook with water, cool and keep the amount visible',
              '<p>For a possible taste, prepare plain oats thoroughly with water and let them cool. Take a small '
              'amount into a separate dish before making your own additions. Thick, hot porridge can cling to a '
              'spoon and does not cool evenly just because its surface feels cooler. Stir and check the whole small '
              "portion rather than bringing a hot spoon to the cat's mouth.</p><p>These are ordinary preparation "
              'precautions, not a feline therapeutic recipe. Avoid offering dry spoonfuls or a hard compressed '
              'cereal bar as if they were equivalent to soft cooked oats. The amount of water changes both texture '
              'and serving weight, so a vague spoonful is not a reproducible energy measure. If a veterinarian '
              'recommends a regular addition, use the specified product and measurement. Do not assume that instant, '
              'steel-cut and flavored packets can all be substituted in the same volume.</p>'),
             ('The packet and topping check matters more than the flavor name',
              '<p>Read instant mixes and ready-made cups all the way through. A raisin-and-spice packet introduces '
              'the issue discussed on our <a href="/can-cats-eat/raisins/">raisin page</a>; chocolate chips '
              'introduce a <a href="/can-cats-eat/chocolate/">chocolate exposure</a>. The oats do not cancel either '
              'concern. <a '
              'href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA\'s '
              'food guidance</a> identifies several ingredients that require care, while our individual pages '
              'explain where feline evidence differs from dog evidence.</p><p>Milk, cream and butter are not '
              "necessary to prepare a cat's possible taste. Many cats do not tolerate dairy well, as discussed on "
              'the <a href="/can-cats-eat/milk/">milk page</a>. Sugar-free syrup also needs the actual ingredient '
              'list; do not turn a generic sweetener warning into an invented feline xylitol dose. If a mixed bowl '
              'has already been eaten, keep every packet and estimate the amount missing. Saying oatmeal alone '
              'leaves out the most useful exposure details.</p>'),
             ('Fiber content does not identify the right gut treatment',
              '<p>Oats contain plant fiber, but a fiber-containing food is not automatically the right choice for '
              'constipation or diarrhea. <a '
              'href="https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals">Merck\'s '
              'nutrition reference</a> explains that fiber differs in its digestive behavior. A kitchen food, a '
              'formulated gastrointestinal diet and a concentrated supplement are not interchangeable simply because '
              'all mention fiber on a label.</p><p>If litter-box changes are the reason for considering oats, ask '
              'the veterinary team what needs investigating and what diet fits the finding. Do not add more cereal '
              'each day to chase a desired stool texture. The <a href="/can-cats-eat/pumpkin/">pumpkin page</a> '
              'explains why another familiar fiber food also needs that distinction. For a well cat, a small oatmeal '
              'taste can remain just a taste, with no digestive-treatment claim attached. That is more accurate than '
              'promising it will soothe a stomach whose problem has not been identified.</p>'),
             ('Keep the main ration and the follow-up clear',
              "<p>Count any oatmeal with the day's other extra foods. The <a "
              'href="/cat-calorie-calculator/">calorie calculator</a> gives an overall starting estimate, not the '
              'calorie density of your particular cooked mixture or permission to replace the normal diet. If you '
              'need to count a repeated serving, use a suitable measured food-energy value and the edible cooked '
              'amount rather than guessing from the size of your breakfast bowl.</p><p>Stop optional additions if '
              'vomiting or diarrhea follows and report repeated symptoms, pain, reduced activity or poor eating to '
              'the clinic. <a href="https://vcahospitals.com/know-your-pet/diarrhea-in-cats">VCA\'s feline diarrhea '
              'guidance</a> emphasizes that the cause guides management. Keep a record of the plain oats and every '
              'topping, plus any other new food offered that day. Do not respond to an unsettled stomach by trying '
              "several cereals in sequence. A stable feeding history and the cat's actual intake give the "
              'veterinarian something useful to work with.</p>')],
 'catnip': [('Why a familiar toy ingredient still deserves a caution label',
             '<p>Catnip is widely used for enrichment, but describing it as unconditionally non-toxic hides an '
             'important qualification. The <a '
             'href="https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/catnip">ASPCA '
             'entry for Nepeta cataria</a> lists nepetalactone and warns of vomiting, diarrhea and either '
             'stimulation or sedation in cats. Our caution is about those possible effects and the way the product '
             'is used. It is not a claim that a catnip toy has the same risk or mechanism as a highly dangerous '
             'plant such as a true lily.</p><p>Read the <a href="/guides/lilies-and-cats/">lily guide</a> for that '
             'separate emergency. Plant names and risk levels should not be blended together. Catnip also is not a '
             'dietary requirement, so a cat that does not respond has nothing missing from its meals. There is no '
             'reason to increase exposure repeatedly to make every cat perform the same rolling or playful behavior '
             'seen in a video.</p>'),
            ('Smelling a toy and eating a pile are different exposures',
             '<p>Choose a simple, identifiable product and read its directions before offering it. A small '
             'catnip-containing toy, loose dried herb, fresh leaves and an extract do not provide the same route or '
             'concentration of exposure. Do not use a familiar name to assume that a bottle of concentrated liquid '
             'can be poured on food or applied directly to the cat. Ask the veterinary team about an unfamiliar '
             'preparation instead of making that conversion yourself.</p><p>For a first enrichment session, keep the '
             'product contained and stay nearby. Let the cat approach or leave voluntarily. Put loose supplies away '
             'afterward, where the cat cannot tear open the packet and eat a large amount without you noticing. This '
             'is practical exposure control, not a published safe-dose schedule. We do not give a grams-per-kilogram '
             'ingestion allowance because this page does not have evidence that would justify one for every '
             'formulation.</p>'),
            ('Inspect the toy, not only the herb inside it',
             '<p>A damaged catnip toy may introduce a problem unrelated to the plant. Check seams, ribbons, string, '
             'detachable decorations and exposed stuffing before play and after rough use. Remove a damaged item '
             'rather than leaving it out because the cat still seems interested. Keep the label or a photograph so '
             'you can describe its contents if something goes missing.</p><p><a '
             'href="https://www.merckvetmanual.com/special-pet-topics/emergencies/minor-injuries-and-accidents">Merck\'s '
             'swallowed-object guidance</a> describes swallowed foreign objects as a separate clinical concern. If '
             'string or part of a toy may have been swallowed, contact a veterinarian even if you initially noticed '
             'the incident because of catnip. Do not give more food as an attempt to push it through or pull at '
             "material protruding from the mouth or anus. A product's pleasant effect does not make its fabric, "
             'plastic or cord edible. Supervision remains useful even for an item marketed specifically to '
             'cats.</p>'),
            ('Observe the individual cat without chasing a stronger response',
             '<p>A quiet response, excited response or lack of interest can all be reasons to end a short session on '
             "the cat's terms. Keep enough space that an aroused cat is not forced into close contact with another "
             'pet. If play becomes uncomfortable or the cat wants to withdraw, take a break rather than adding more '
             'herb. Choose an ordinary toy or a different interaction next time if catnip does not suit the '
             'household.</p><p>Do not use catnip to conceal an ongoing behavioral or medical change. A cat hiding '
             'more, eating less or changing its litter-box habits needs attention to that change; a brief response '
             'to a toy does not rule out illness. The <a href="/guides/senior-cat-weight-and-appetite/">senior '
             'appetite guide</a> can help structure observations. Enrichment is valuable as an activity, but it is '
             'not a diagnosis or a replacement for an appropriate care plan.</p>'),
            ('After ingestion or an unexpected reaction',
             '<p>If a cat eats loose herb and vomits or develops diarrhea, remove the product and contact your '
             'veterinarian for advice about the amount, timing and signs. Keep the packaging and mention extracts, '
             'sprays or additional ingredients. Severe distress, breathing difficulty, collapse or suspected toy '
             'ingestion needs urgent attention rather than an assumption that the response is a normal catnip '
             'episode.</p><p>The <a href="/guides/how-catcalc-rates-human-foods/">rating method</a> explains why '
             'this site distinguishes toxicity, physical injury and uncertainty. Catnip does not need a calorie '
             'allowance calculated like <a href="/can-cats-eat/chicken/">a cooked-chicken treat</a>, and it should '
             'not be added to meals to fill a snack budget. If eating or weight is the concern, use the <a '
             'href="/cat-calorie-calculator/">calorie calculator</a> only for its stated planning role and discuss '
             'the actual problem with the clinic. Keep enrichment products and nutritional decisions separate.</p>')]}
