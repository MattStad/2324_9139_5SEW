package WH_Test;

/**
 * @author Matthias
 * @Klasse 5CN
 */

public class Input {
    private boolean state;
    private Gate gate;

    public Input(Gate gate) {
        this.gate = gate;
    }

    /**
     * Liefert den state zurück
     *
     * @return state
     */
    public boolean getState() {
        return state;
    }

    /**
     * Ändert den State
     *
     * @param state
     */
    public void setState(boolean state) {
        this.state = state;
        gate.calcState();
    }
}
