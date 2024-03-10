### HW08 - Currency Converter

#### **Problem Description**

For this assignment, you will fill in the blanks of a nearly completed JavaFX program so that it functions as shown in the two images below:

<p align="center">
<img src="https://lh5.googleusercontent.com/GcW8pbWhLlxb5-WlDlPbltrTdcYR8dyIeiXdzojc24l477lbQuBiqWHBlJ7m1iuIGGCBQpEosXEO1E0OcREnE6i1u6OkibW8ET8f4IZTN1Zftx9hgwcVyjndtMnimvWbKGHZv5v4" width="400">
<br>  <br>
<img src="https://lh6.googleusercontent.com/8FikQYO2lMBulRruxywSvy_y4nqplWT2kH3dh-2-yULHFhi089qt3obNcKy9idOSr-fAuuB73dIY05fCUEsuir_YtBWI8-j7O8muApIAdysR5jAQQClsijevw8lhf2SDqxWWlT7i" width="400">
</p>

As shown, the program converts a Dollar input value to its corresponding Pound value. Once the user clicks the Exchange button, the input value is converted and the Pound value is printed below the button. If the user inputs a non-numeric value, an error message is displayed.

---

### Here is the program with blanks:

```
import javafx.application.______1_____;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.______2_______;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout._____3______;
import javafx.scene.text.Text;
import javafx.scene.control.Label;
import javafx.stage.Stage;

  public class DollarsToPounds extends _______4_______ {

      final static double EXCHANGE_RATE = 0.81;

      public void _____5____(_____6_____ stage) {

      Label valueLbl = new Label(____7_____);

      Label poundsLbl = new Label();

      ______8______ dollarsTxt = new ____9______();

      Button ____10_____ = new Button();

      exchangeBtn.____11____(______12______);

      _______13______(____14_____ {
         String dollarsStr = ______15______.toString();
         try {
              double dollars = Double.parseDouble(dollarsStr);
              double pounds = ____16_____(dollars);
              poundsLbl.setText(String.format("%.2f", pounds));
             } catch (NumberFormatException e) {
                    ___17___ a = new ____18____(___19_____);
                    _____20______("Error");
                     a.setHeaderText("Invalid Dollar Amount");
                     a.setContentText("Please only use digits.");
                     a.showAndWait();
            }
        });

        ___21___ input = new _____22_____();
        input.setAlignment(Pos.CENTER);
        _______23_____(valueLbl, _____24_____);

        _____25_____ root = new ____26____();
        root.setAlignment(Pos.CENTER);
        root.setSpacing(8);
        root._____27____(_______28________, ________29________, ________30_______);

        _____31____ scene = new _____32_____(____33_____, 400, 400);
        _______34____("Dollars to Pounds");
        stage.setScene(____35___);
        stage.show();

    }

    private double exchange(double dollars) {
       return dollars*_______36________;
    }
}
```
