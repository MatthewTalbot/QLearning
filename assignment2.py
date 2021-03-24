def fuzzy_classifier(dog_characteristics):
    #girth
    girth_small = [0,0,40,50]
    girth_medium = [40,50,60,70]
    girth_large = [60,70,100,100]
    #height
    height_short = [0,0,25,40]
    height_medium = [25,40,50,60]
    height_tall = [50,60,100,100]
    #weight
    weight_light = [0,0,5,15]
    weight_medium = [5,15,20,40]
    weight_heavy = [20,40,100,100]

    #Fuzzify the crisp input(dog_characteristics is the crisp input)
    m_girth_small = membership(dog_characteristics[0], girth_small)
    m_girth_medium = membership(dog_characteristics[0], girth_medium)
    m_girth_large = membership(dog_characteristics[0], girth_large)

    m_height_short = membership(dog_characteristics[1], height_short)
    m_height_medium = membership(dog_characteristics[1], height_medium)
    m_height_tall = membership(dog_characteristics[1], height_tall)

    m_weight_light = membership(dog_characteristics[2], weight_light)
    m_weight_medium = membership(dog_characteristics[2], weight_medium)
    m_weight_heavy = membership(dog_characteristics[2], weight_heavy)

    #Compute the rule Strengths
    #Rule 1: IF height is medium AND (girth is small OR weight is light) THEN beagle.
    rule_1_strength = t_norm(m_height_medium, s_norm(m_girth_small,m_weight_light))
    #Rule 2: IF girth is medium AND height is short AND weight is medium THEN corgi.
    rule_2_strength = t_norm(m_girth_medium, t_norm(m_height_short,m_weight_medium))
    #Rule 3: IF girth is large AND height is tall AND weight is medium THEN husky.
    rule_3_strength = t_norm(m_girth_large,t_norm(m_height_tall,m_weight_medium))
    #Rule 4: IF (girth is medium OR height is medium) AND weight is heavy THEN poodle.
    rule_4_strength = t_norm(s_norm(m_girth_medium,m_height_medium),m_weight_heavy)

    #Combine the rule Strengths
    m_combined = [rule_1_strength, rule_2_strength, rule_3_strength, rule_4_strength]

    return argmax(m_combined)

#Membership funciton
def membership(x, list):
  if x <= list[0]:
    return 0

  if list[0] < x and x < list[1]:
    return (x-list[0])/(list[1]-list[0])

  if list[1] <= x and x <= list[2]:
    return 1

  if list[2] < x and x < list[3]:
    return (list[3]-x)/(list[3]-list[2])

  if list[3] <= x:
    return 0

#Goguem t and s norm
def t_norm(x,y):
  return min(x,y)

def s_norm(x,y):
  return max(x,y)

#Returns the argmax of m_combined
#[0,1,2,3,4,5,4,3,2,1,5]
def argmax(m_combined):
  max_list = [i for i, x in enumerate(m_combined) if x==max(m_combined)]
  dog_list = ["beagle", "corgi", "husky", "poodle"]
  final_list = []

  for pos in max_list:
    final_list.append(dog_list[pos])
  
  if len(final_list) > 1:
    return "More than one max value found. Therefore each of these breeds is equally likely", final_list, m_combined

  return final_list[0], m_combined

#Testing
def main():
  dog_characteristics = [65, 45, 30]
  print(fuzzy_classifier(dog_characteristics))

main()
