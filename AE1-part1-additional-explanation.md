
# Bitmap

* A sequence of bits, ordered left to right
* Grouped in bytes

		00011011 01000101 01100111 11 ...

* Bitmap index is 2 bytes
* Getting the index of the byte:

		idx>>3 (i.e. idx/8)

* Getting a bit out of a byte is byte-level operation

		<idx> NIP 

	removes the MSB from the index

* For example, say the bit index is `174`

		#00ae ( 174 in dec )

	The byte index is `174/8=21` (integer division)

		#00ae #0008 DIV2 ( 0015, 21 in dec )

	The bit index is `174-21*8=6`

		#00ae #00ae #0008 DIV2 #0008 MUL2 SUB2 ( 0006 )

	or better

		#00ae DUP2 #0008 DIV2 #0008 MUL2 SUB2 ( 0006 )

	We only need the LSB so we use `NIP`

		#00ae DUP2 #0008 DIV2 #0008 MUL2 SUB2 NIP ( 06 )

## Bit shift operations	

Instead of `((x/8)*<<*8)` we can use shift operations: `((x>>3)<<3)`. In Uxntal:

		<byte> <how much to shift, byte> SFT

	or

		<short> <how much to shift, byte> SFT2

* How much to shift:

		shift to left = upper nibble
		shift to right = lower nibble

		e.g shift 5 to right (x>>5) 

			#05 SFT
			
		e.g shift 5 to left (x<<5) 

			#50 SFT

* Which means that we can write the above as			

		#00ae #0008 DIV2 #0008 MUL2

	or as

		#00ae #03 SFT2 #30 SFT2

	or even as 

		#00ae #33 SFT2

* Suppose we have `#05`, how to get to `#50`?

	Shift to left over 4 positions!

		#05 #40 SFT == #50

	So in general, 

		<n-bits-to-shift> SFT = right shift
		<n-bits-to-shift> #40 SFT SFT = left shift

