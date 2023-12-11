package WH_Test;

/**
 * input 0 = set
 * input 1 = reset
 *
 * @author Matthias Stadlinger
 */
public class FlipFlop extends Gate {

    private boolean state;

    public FlipFlop(String name) {
        super(name, 2, 2);
    }

    @Override
    public void dispatch() {
        setState(0, state);
        setState(1, !state);
    }

    @Override
    void calcState() {
        if (inputs[0] != null && inputs[0].getState()) {
            state = true;
        } else if (inputs[1] != null && inputs[1].getState()) {
            state = false;
        }
        dispatch();
    }
}
