def convert_heights_nested(h_incs):
    h_cms = []

    for i in h_incs:
        cm = round(i * 2.54, 2)
        h_cms.append(cm)

    return h_cms

def convert_heights_comprehension(h_inchs):
    h_Centis = [round(inch * 2.54, 2) for inch in h_inchs]

    return h_Centis

def main():
    h_incs = []
    no_cust = int(input("Enter the no.of custs: "))

    for i in range(no_cust):
        hei = float(input(f"Enter height for customer {i+1} in inches: "))
        h_incs.append(hei)

    h_cms_ntd = convert_heights_nested(h_incs)
    print("Heights in centimeters using Nested Loop:", h_cms_ntd)

    h_cms_comp = convert_heights_comprehension(h_incs)
    print("Heights in centimeters using List Comprehension:", h_cms_comp)

if __name__ == "__main__":
    main()
