package WH_Test;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Matthias
 * @Klasse 5CN
 */

public class Output {
    private final List<Input> in = new ArrayList<>();

    public Output() {
    }

    /**
     * Weist die Inputs zu die an den Output angeschlossen sind
     *
     * @param in Input
     */
    public void addInput(Input in) {
        this.in.add(in);
    }

    /**
     * Ändert den State
     *
     * @param state
     */
    public void setState(boolean state) {
        for (Input i:in) {
            i.setState(state);
        }
    }

    /**
     * Liefert den State zurück
     *
     * @return state
     */
    public boolean getState() {
        return in.get(0).getState();
    }
}
