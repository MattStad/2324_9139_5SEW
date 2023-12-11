package WH_Test;

/**
 * @author Matthias
 * @Klasse 5CN
 */
public class LED extends Gate {
    boolean state = false;

    public LED(String name) {
        super(name, 1, 0);
    }

    @Override
    public void dispatch() {

    }

    @Override
    void calcState() {
        state = inputs[0].getState();
    }

    /**
     * Fragt ab ob die LED an oder aus ist
     *
     * @return state
     */
    public boolean isOn() {
        return state;
    }
}
