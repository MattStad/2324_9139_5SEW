package WH_Test;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * @author Matthias
 * @Klasse 5CN
 */
public class TestLED {
    @Test
    void OneButtonOneLED() {
        Taster taster = new Taster("Taster");
        LED led = new LED("LED");
        taster.connect(0, led, 0);

        taster.press();
        assertTrue(led.isOn());
        taster.press();
        assertFalse(led.isOn());
    }

    @Test
    void TwoButtonTwoLED() {
        Taster taster1 = new Taster("Taster1");
        Taster taster2 = new Taster("Taster2");
        LED led1 = new LED("LED1");
        LED led2 = new LED("LED2");
        taster1.connect(0, led1, 0);
        taster2.connect(0, led2, 0);

        taster1.press();
        taster2.press();
        assertTrue(led1.isOn());
        assertTrue(led2.isOn());
        taster1.press();
        taster2.press();
        assertFalse(led1.isOn());
        assertFalse(led2.isOn());
    }

    @Test
    void OneButtonTwoLED() {
        Taster taster1 = new Taster("Taster1");
        LED led1 = new LED("LED1");
        LED led2 = new LED("LED2");
        taster1.connect(0, led1, 0);
        taster1.connect(0, led2, 0);

        taster1.press();
        assertTrue(led1.isOn());
        assertTrue(led2.isOn());
        taster1.press();
        assertFalse(led1.isOn());
        assertFalse(led2.isOn());
    }

    @Test
    void WholeCurcuit() {
        Taster tasterS = new Taster("TasterS");
        Taster tasterR = new Taster("TasterR");
        FlipFlop flipFlop = new FlipFlop("FF");

        tasterS.connect(0, flipFlop, 0);
        tasterR.connect(0, flipFlop, 1);

        LED led = new LED("LED");
        flipFlop.connect(0, led, 0);

        tasterS.press();
        assertTrue(led.isOn());
        tasterS.press();
        assertTrue(led.isOn());
        tasterR.press();
        assertFalse(led.isOn());
        tasterR.press();
        assertFalse(led.isOn());
        tasterS.press();
        tasterR.press();
        assertTrue(led.isOn());
    }

    @Test
    void TestnotQOutput() {
        Taster tasterS = new Taster("TasterS");
        Taster tasterR = new Taster("TasterR");

        FlipFlop flipFlop = new FlipFlop("FF");


        tasterS.connect(0, flipFlop, 0);
        tasterR.connect(0, flipFlop, 1);

        LED led = new LED("LED");
        flipFlop.connect(1, led, 0);

        tasterS.press();
        assertFalse(led.isOn());
        tasterR.press();
        assertFalse(led.isOn());
        tasterS.press();
        assertTrue(led.isOn());
        tasterR.press();
        assertTrue(led.isOn());
    }
}
