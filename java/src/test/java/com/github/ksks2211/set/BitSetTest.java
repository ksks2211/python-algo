package com.github.ksks2211.set;

import org.junit.jupiter.api.Test;

import java.util.BitSet;

import static org.junit.jupiter.api.Assertions.*;

/**
 * @author rival
 * @since 2024-06-03
 */
public class BitSetTest {


    @Test
    public void test() {

        BitSet bitSet = new BitSet();

        bitSet.set(0);
        bitSet.set(1);
        bitSet.set(2);

        assertEquals(3, bitSet.length());

        assertFalse(bitSet.isEmpty());
        assertTrue(bitSet.get(0));
        assertFalse(bitSet.get(3));

        bitSet.clear(0);
        assertFalse(bitSet.get(0));

        



    }
}
