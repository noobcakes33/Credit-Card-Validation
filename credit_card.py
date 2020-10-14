class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.start_n = [4,5,6]
        self.digits_n = '0 1 2 3 4 5 6 7 8 9'.split()
        self.digit_checker = 0
        self.c = ''
        self.valid = 0
        self.process_numbers(card_number)
        self.validate()

    def process_numbers(self, card_number):
        """Removes the hyphen from the card number string"""
        self.card = card_number.split('-')
        for n in self.card:
            self.c += n


    def valid_seq(self):
        """checks if all sequences of the card number are 4"""
        #print(self.card_number)
        if '-' in self.card_number:
            for seq in self.card:
                if len(seq) != 4:
                    #print("[valid_seq] False")
                    return False
        #print("[valid_seq] True")
        return True


    def valid_start(self):
        """Ensures the first number of the card containing 4, 5, or 6"""
        #print("[valid_start] ", int(self.c[0]) in self.start_n)
        return int(self.c[0]) in self.start_n


    def num_length(self):
        """Ensures the length of the card numbers is 16"""
        #print("[num_length] ", len(self.c) == 16)
        return len(self.c) == 16


    def digits(self):
        """Checks if all the characters in the card number are valid numbers not special characters or spaces"""
        for num in self.c:
            if num in self.digits_n:
                self.digit_checker += 1
        #print("[digits] ", self.digit_checker == 16)
        return self.digit_checker == 16


    def check_repeated(self):
        """Checks if the card number has 4 or more consecutive repeated digits"""
        counter = 0
        for i in range(len(self.c)):
            try:
                n = self.c[i]
                for j in range(4):
                    if self.c[i+j] == n:
                        counter +=1

                if counter >=4:
                    #print("[check_repeated] True")
                    return True
                else:
                    counter = 0
            except:
                pass
        #print("[check_repeated] False")
        return False

    def validate(self):
        """"Validates the card number"""
        self.valid = self.valid_seq() + self.valid_start() + self.num_length() + self.digits() + self.check_repeated()
        if self.valid == 4:
            print("Valid")
        else:
            print("Invalid")


if __name__ == "__main__":
    sample_inputs = ['4123456789123456',
                     '5123-4567-8912-3456',
                     '61234-567-8912-3456',
                     '4123356789123456',
                     '5133-3367-8912-3456',
                     '5123 - 3567 - 8912 - 3456']
    for sample in sample_inputs:
        card = CreditCard(sample)
