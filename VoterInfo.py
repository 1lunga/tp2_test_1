update_voter_info=[]
def voter_id(id):
    voter_id.append({"Voter ID:",int("Enter Voter ID:",id) })
def vname(votername):
    vname.append({"Name:", ("Enter Voter's name:",votername)})
def voting_district(district):
    voting_district.append({"District:",("Enter District",district)})
def has_voted(voted):
    has_voted.append({"Has Voted:",("Voted/Not Voted",voted)})

print("Registered Voter:", update_voter_info)