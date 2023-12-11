package WH_Test;

/**
 * @author Matthias
 * @Klasse 5CN
 */


abstract public class Gate {
    int nInputs;
    int nOutputs;
    Input[] inputs;
    Output[] outputs;
    String name;

    /**
     * Konstruktor
     *
     * @param name
     * @param nInputs  Anzahl an Inputs
     * @param nOutputs Anzahl an Outputs
     */
    public Gate(String name, int nInputs, int nOutputs) {
        this.nInputs = nInputs;
        this.nOutputs = nOutputs;
        this.name = name;
        this.inputs = new Input[nInputs];
        this.outputs = new Output[nOutputs];
    }

    /**
     * Überprüfto ob pin existiert und wenn schon ruft es setState() auf
     *
     * @param pin
     * @param state
     */
    public void setState(int pin, boolean state) {
        if (nOutputs > pin && pin >= 0) {
            if (outputs[pin] == null) {
                outputs[pin] = new Output();
            }
            outputs[pin].setState(state);
        }
    }

    /**
     * sendet die neuen berechneten Zustände von den Outputs an die Inputs des nächsten Gates
     */
    public abstract void dispatch();

    @Override
    public String toString() {
        String out = name + ":";
        for (int i = 0; i < inputs.length; i++) {
            out += inputs[i].getState();
        }
        out += "/";
        for (int i = 0; i < outputs.length; i++) {
            out += outputs[i].getState();
        }
        return out;
    }

    /**
     * Verbindet Outputs mit inputs
     *
     * @param outPort      welcher Output soll verwendet werden
     * @param receiverGate an welches Bauteil soll es gehen
     * @param receiverPin  an welchen Pin soll es gehen
     */
    public void connect(int outPort, Gate receiverGate, int receiverPin) {
        if (outPort < nOutputs && receiverPin < receiverGate.nInputs) {
            if (outputs[outPort] == null) this.outputs[outPort] = new Output();
            Input in = receiverGate.inputs[receiverPin] != null ? receiverGate.inputs[receiverPin] : new Input(receiverGate);
            this.outputs[outPort].addInput(in);
            receiverGate.inputs[receiverPin] = in;
        }
    }

    /**
     * brechnet den zukünftigen Zustand
     */
    abstract void calcState();
}
