#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Collect
# Generated: Thu Jul 21 21:14:47 2011
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser

class collect(gr.top_block):

	def __init__(self, agc_max=100, agc_decay=0.1, freq_offset=1000000, outfile="datafifo", bandpass_bandwidth=20, threshold_buffer=0.25, threshold_center=0.5, agc_attack=0.1, bandpass_transition_width=1000000):
		gr.top_block.__init__(self, "Collect")

		##################################################
		# Parameters
		##################################################
		self.agc_max = agc_max
		self.agc_decay = agc_decay
		self.freq_offset = freq_offset
		self.outfile = outfile
		self.bandpass_bandwidth = bandpass_bandwidth
		self.threshold_buffer = threshold_buffer
		self.threshold_center = threshold_center
		self.agc_attack = agc_attack
		self.bandpass_transition_width = bandpass_transition_width

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 64000000

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			io_type=uhd.io_type.COMPLEX_FLOAT32,
			num_channels=1,
		)
		self.uhd_usrp_source_0.set_samp_rate(samp_rate)
		self.uhd_usrp_source_0.set_center_freq(915000000 - freq_offset, 0)
		self.uhd_usrp_source_0.set_gain(0, 0)
		self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
		self.gr_threshold_ff_0 = gr.threshold_ff(threshold_center - threshold_buffer, threshold_center + threshold_buffer, 0)
		self.gr_map_bb_0 = gr.map_bb(([48, 49]))
		self.gr_float_to_char_0 = gr.float_to_char()
		self.gr_file_sink_0 = gr.file_sink(gr.sizeof_char*1, outfile)
		self.gr_file_sink_0.set_unbuffered(False)
		self.gr_complex_to_mag_0 = gr.complex_to_mag(1)
		self.gr_agc2_xx_0_0 = gr.agc2_cc(agc_attack, agc_decay, 1.0, 1.0, agc_max)
		self.band_pass_filter_0 = gr.fir_filter_ccf(1, firdes.band_pass(
			1, samp_rate, freq_offset-bandpass_bandwidth/2, freq_offset+bandpass_bandwidth/2, bandpass_transition_width, firdes.WIN_HAMMING, 6.76))

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_float_to_char_0, 0), (self.gr_map_bb_0, 0))
		self.connect((self.gr_map_bb_0, 0), (self.gr_file_sink_0, 0))
		self.connect((self.uhd_usrp_source_0, 0), (self.gr_agc2_xx_0_0, 0))
		self.connect((self.gr_agc2_xx_0_0, 0), (self.band_pass_filter_0, 0))
		self.connect((self.gr_threshold_ff_0, 0), (self.gr_float_to_char_0, 0))
		self.connect((self.gr_complex_to_mag_0, 0), (self.gr_threshold_ff_0, 0))
		self.connect((self.band_pass_filter_0, 0), (self.gr_complex_to_mag_0, 0))

	def get_agc_max(self):
		return self.agc_max

	def set_agc_max(self, agc_max):
		self.agc_max = agc_max
		self.gr_agc2_xx_0_0.set_max_gain(self.agc_max)

	def get_agc_decay(self):
		return self.agc_decay

	def set_agc_decay(self, agc_decay):
		self.agc_decay = agc_decay
		self.gr_agc2_xx_0_0.set_decay_rate(self.agc_decay)

	def get_freq_offset(self):
		return self.freq_offset

	def set_freq_offset(self, freq_offset):
		self.freq_offset = freq_offset
		self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.freq_offset-self.bandpass_bandwidth/2, self.freq_offset+self.bandpass_bandwidth/2, self.bandpass_transition_width, firdes.WIN_HAMMING, 6.76))
		self.uhd_usrp_source_0.set_center_freq(915000000 - self.freq_offset, 0)

	def get_outfile(self):
		return self.outfile

	def set_outfile(self, outfile):
		self.outfile = outfile

	def get_bandpass_bandwidth(self):
		return self.bandpass_bandwidth

	def set_bandpass_bandwidth(self, bandpass_bandwidth):
		self.bandpass_bandwidth = bandpass_bandwidth
		self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.freq_offset-self.bandpass_bandwidth/2, self.freq_offset+self.bandpass_bandwidth/2, self.bandpass_transition_width, firdes.WIN_HAMMING, 6.76))

	def get_threshold_buffer(self):
		return self.threshold_buffer

	def set_threshold_buffer(self, threshold_buffer):
		self.threshold_buffer = threshold_buffer
		self.gr_threshold_ff_0.set_hi(self.threshold_center + self.threshold_buffer)
		self.gr_threshold_ff_0.set_lo(self.threshold_center - self.threshold_buffer)

	def get_threshold_center(self):
		return self.threshold_center

	def set_threshold_center(self, threshold_center):
		self.threshold_center = threshold_center
		self.gr_threshold_ff_0.set_hi(self.threshold_center + self.threshold_buffer)
		self.gr_threshold_ff_0.set_lo(self.threshold_center - self.threshold_buffer)

	def get_agc_attack(self):
		return self.agc_attack

	def set_agc_attack(self, agc_attack):
		self.agc_attack = agc_attack
		self.gr_agc2_xx_0_0.set_attack_rate(self.agc_attack)

	def get_bandpass_transition_width(self):
		return self.bandpass_transition_width

	def set_bandpass_transition_width(self, bandpass_transition_width):
		self.bandpass_transition_width = bandpass_transition_width
		self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.freq_offset-self.bandpass_bandwidth/2, self.freq_offset+self.bandpass_bandwidth/2, self.bandpass_transition_width, firdes.WIN_HAMMING, 6.76))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.freq_offset-self.bandpass_bandwidth/2, self.freq_offset+self.bandpass_bandwidth/2, self.bandpass_transition_width, firdes.WIN_HAMMING, 6.76))
		self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("", "--agc-max", dest="agc_max", type="eng_float", default=eng_notation.num_to_str(100),
		help="Set AGC Max Gain [default=%default]")
	parser.add_option("", "--agc-decay", dest="agc_decay", type="eng_float", default=eng_notation.num_to_str(0.1),
		help="Set AGC Decay Rate [default=%default]")
	parser.add_option("-f", "--freq-offset", dest="freq_offset", type="eng_float", default=eng_notation.num_to_str(1000000),
		help="Set Offset below 915MHz [default=%default]")
	parser.add_option("-o", "--outfile", dest="outfile", type="string", default="datafifo",
		help="Set Output File [default=%default]")
	parser.add_option("", "--bandpass-bandwidth", dest="bandpass_bandwidth", type="eng_float", default=eng_notation.num_to_str(20),
		help="Set Band Pass Filter Bandwidth [default=%default]")
	parser.add_option("", "--threshold-buffer", dest="threshold_buffer", type="eng_float", default=eng_notation.num_to_str(0.25),
		help="Set Threshold Buffer [default=%default]")
	parser.add_option("", "--threshold-center", dest="threshold_center", type="eng_float", default=eng_notation.num_to_str(0.5),
		help="Set Threshold Center [default=%default]")
	parser.add_option("", "--agc-attack", dest="agc_attack", type="eng_float", default=eng_notation.num_to_str(0.1),
		help="Set AGC Attack Rate [default=%default]")
	parser.add_option("-w", "--bandpass-transition-width", dest="bandpass_transition_width", type="eng_float", default=eng_notation.num_to_str(1000000),
		help="Set Band Pass Filter Transition Width [default=%default]")
	(options, args) = parser.parse_args()
	tb = collect(agc_max=options.agc_max, agc_decay=options.agc_decay, freq_offset=options.freq_offset, outfile=options.outfile, bandpass_bandwidth=options.bandpass_bandwidth, threshold_buffer=options.threshold_buffer, threshold_center=options.threshold_center, agc_attack=options.agc_attack, bandpass_transition_width=options.bandpass_transition_width)
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()

