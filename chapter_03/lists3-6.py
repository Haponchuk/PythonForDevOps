# 3-4
guests = ['Leon', 'Spike', 'Mortis']
print(f'Hi {guests[0]}, {guests[1]} and {guests[2]}. I\'d like to invite you to have a dinner with me.')

# 3-5 
guests2 = ['Leon', 'Spike', 'Mortis']
print(f'{guests2[0]} and {guests2[2]} can\'t come to dinner with us')

guests2[0] = 'Frank'
guests2[2] = 'Meg'
print(f'Hi {guests[0]} and {guests[2]}. I\'d like to invite you to have a dinner with us.')

# 3-6
guests3 = ['Leon', 'Spike', 'Mortis']
print(f'Yoo, guys. I fount a bigger table so we can invite more ppl!')

guests3.insert(0, 'Bibi')
guests3.insert(1, 'Jess')
guests3.append('Crow')
print(f'{guests3[0]}, {guests3[1]} and {guests3[-1]} come to dinner with us, guys')

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.
# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.