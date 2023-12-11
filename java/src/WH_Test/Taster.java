package WH_Test;

/**
 * @author Matthias
 * @Klasse 5CN
 */
public class Taster extends Gate {
    public Taster(String name) {
        super(name, 0, 1);
    }

    @Override
    public void dispatch() {
    }

    @Override
    void calcState() {
    }

    /**
     * Drückt den Taster und ändert somit den State
     */
    public void press() {
        setState(0, !outputs[0].getState());
    }
}
