import java.util.NoSuchElementException;

public class ExternalChainingHashMap<K, V> {

    public static final int INITIAL_CAPACITY = 13;

    public static final double MAX_LOAD_FACTOR = 0.67;

    private ExternalChainingMapEntry<K, V>[] table;
    private int size;

    public ExternalChainingHashMap() {
        table = (ExternalChainingMapEntry<K, V>[]) new ExternalChainingMapEntry[INITIAL_CAPACITY];
    }

    public V put(K key, V value) {
        if (key == null || value == null) { throw new IllegalArgumentException(); }

        if ((double) (this.size + 1) / this.table.length > MAX_LOAD_FACTOR) {
            resizeBackingTable((2 * this.table.length) + 1);
        }
        
        int index = Math.abs(key.hashCode() % this.table.length);

        var current = this.table[index];
        while (current != null) {
            if (current.getKey().equals(key)) {
                V oldValue = current.getValue();
                current.setValue(value);
                return oldValue;
            }
            current = current.getNext();
        }
        var oldHead = this.table[index];
        this.table[index] = new ExternalChainingMapEntry<K, V>(key, value, oldHead);
        this.size++;
        return null;
    }

    public V remove(K key) {
        if (key == null) { throw new java.lang.IllegalArgumentException(); }
        int index = Math.abs(key.hashCode() % this.table.length);

        if (this.table[index] == null) {
            throw new java.util.NoSuchElementException(); 
        }

        if (this.table[index].getKey().equals(key)) {
            var value = this.table[index].getValue();
            this.table[index] = this.table[index].getNext();
            this.size--;
            return value;
        }

        var previous = this.table[index];
        var current = this.table[index].getNext();
        while (current != null) {
            if (current.getKey().equals(key)) {
                var value = current.getValue();
                previous.setNext(current.getNext());
                this.size--;
                return value;
            }
            previous = current;
            current = current.getNext();
        }
      
        throw new NoSuchElementException();
    }

    private void resizeBackingTable(int length) {
        var newTable = (ExternalChainingMapEntry<K, V>[]) new ExternalChainingMapEntry[length];
        for (ExternalChainingMapEntry<K, V> entry : this.table) {
            var current = entry;
            while (current != null) {
                int index = Math.abs(current.getKey().hashCode() % length);
                ExternalChainingMapEntry<K, V> node = new ExternalChainingMapEntry<K, V>(current.getKey(),
                        current.getValue(), newTable[index]);
                newTable[index] = node;
                current = current.getNext();
            }
        }
        this.table = newTable;
    }

    public ExternalChainingMapEntry<K, V>[] getTable() {
        return table;
    }

    public int size() {
        return size;
    }
}
