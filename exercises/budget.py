from typing import Dict


class Budget:
    dad_income: int
    mom_income: int
    expenses: Dict[str, int]

    def __init__(self, dad: int, mom: int, expenses: Dict[str, int]):
        self.dad_income = dad
        self.mom_income = mom
        self.expenses = expenses

    def find_deficit(self, predicted_exp: Dict[str, int], actual_exp: Dict[str, int]) -> Dict[str, int]:
        """A method that finds the higher expense."""
        found_difference: Dict[str, int] = {}
        for category in actual_exp:
            for type in predicted_exp:
                if category == type:
                    if predicted_exp[type] != actual_exp[category]:
                        found_difference[type] = predicted_exp[category] - actual_exp[type]
        return found_difference

    def expenses_vs_income(self) -> int:
        total_expenses: int = 0
        for i in self.expenses:
            total_expenses += self.expenses[i]
        difference : int = (self.dad_income + self. mom_income) - total_expenses
        return difference
    
    def predicted_vs_income(self, predited: Dict[str, int]) -> int:
        total_expenses: int = 0
        for i in predited:
            total_expenses += predited[i]
        difference : int = (self.dad_income + self. mom_income) - total_expenses
        return difference


def main() -> None:
    d_income: int = 2880
    m_income: int = 2808
    expenses: Dict[str, int] = {"Renta": 778, "Luz": 80, "Agua": 60, "Gas": 80, "Spectrum": 71,
    "Seguro de Salud": 150, "Seguro Carros": 240, "Prestamo Carro": 257, "Prestamo Personal" : 207,
    "Tarjetas Ivette": 350, "Tarj Julio": 150, "Gasolina": 320, "Jardineria": 100, "Comida": 840, "Celulares": 135,
    "Meds": 164}
    house_budg: Budget = Budget(d_income, m_income, expenses)
    predicted: Dict[str, int] = {"Renta": 778, "Luz": 80, "Agua": 60, "Gas": 80, "Spectrum": 71,
    "Seguro de Salud": 150, "Seguro Carros": 240, "Prestamo Carro": 257, "Prestamo Personal" : 207,
    "Tarjetas Ivette": 350, "Tarj Julio": 250, "Gasolina": 320, "Jardineria": 100, "Comida": 840, "Celulares": 135,
    "Meds": 164}
    total_pred: int = 0
    for i in predicted:
        total_pred += predicted[i]
    print(total_pred)
    print(house_budg.find_deficit(predicted, expenses))
    sur_def: int = house_budg. expenses_vs_income()
    if sur_def >= 0:
        print("surplos of " + str(sur_def))
    else:
        print("deficit of " + str(sur_def))
    print(house_budg. predicted_vs_income(predicted))


if __name__ == "__main__":
    main()




