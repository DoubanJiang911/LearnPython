class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        categorize = []
        for element in [length, width, height, mass]:
            if element >= 10**4:
                categorize.append("Bulky")
                break
        if categorize:
            pass
        elif length*width*height >= 10**9:
            categorize.append("Bulky")
        else:
            pass
        if mass >= 100:
            categorize.append("Heavy")
        match len(categorize):
            case 2:
                return "Both"
            case 1:
                return categorize[0]
            case 0:
                return "Neither"
