# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: confirmed_block.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63onfirmed_block.proto\x12\x1dsolana.storage.ConfirmedBlock\"\xdb\x02\n\x0e\x43onfirmedBlock\x12\x1a\n\x12previous_blockhash\x18\x01 \x01(\t\x12\x11\n\tblockhash\x18\x02 \x01(\t\x12\x13\n\x0bparent_slot\x18\x03 \x01(\x04\x12I\n\x0ctransactions\x18\x04 \x03(\x0b\x32\x33.solana.storage.ConfirmedBlock.ConfirmedTransaction\x12\x36\n\x07rewards\x18\x05 \x03(\x0b\x32%.solana.storage.ConfirmedBlock.Reward\x12@\n\nblock_time\x18\x06 \x01(\x0b\x32,.solana.storage.ConfirmedBlock.UnixTimestamp\x12@\n\x0c\x62lock_height\x18\x07 \x01(\x0b\x32*.solana.storage.ConfirmedBlock.BlockHeight\"\x9b\x01\n\x14\x43onfirmedTransaction\x12?\n\x0btransaction\x18\x01 \x01(\x0b\x32*.solana.storage.ConfirmedBlock.Transaction\x12\x42\n\x04meta\x18\x02 \x01(\x0b\x32\x34.solana.storage.ConfirmedBlock.TransactionStatusMeta\"Z\n\x0bTransaction\x12\x12\n\nsignatures\x18\x01 \x03(\x0c\x12\x37\n\x07message\x18\x02 \x01(\x0b\x32&.solana.storage.ConfirmedBlock.Message\"\xad\x02\n\x07Message\x12<\n\x06header\x18\x01 \x01(\x0b\x32,.solana.storage.ConfirmedBlock.MessageHeader\x12\x14\n\x0c\x61\x63\x63ount_keys\x18\x02 \x03(\x0c\x12\x18\n\x10recent_blockhash\x18\x03 \x01(\x0c\x12H\n\x0cinstructions\x18\x04 \x03(\x0b\x32\x32.solana.storage.ConfirmedBlock.CompiledInstruction\x12\x11\n\tversioned\x18\x05 \x01(\x08\x12W\n\x15\x61\x64\x64ress_table_lookups\x18\x06 \x03(\x0b\x32\x38.solana.storage.ConfirmedBlock.MessageAddressTableLookup\"~\n\rMessageHeader\x12\x1f\n\x17num_required_signatures\x18\x01 \x01(\r\x12$\n\x1cnum_readonly_signed_accounts\x18\x02 \x01(\r\x12&\n\x1enum_readonly_unsigned_accounts\x18\x03 \x01(\r\"d\n\x19MessageAddressTableLookup\x12\x13\n\x0b\x61\x63\x63ount_key\x18\x01 \x01(\x0c\x12\x18\n\x10writable_indexes\x18\x02 \x01(\x0c\x12\x18\n\x10readonly_indexes\x18\x03 \x01(\x0c\"\xda\x05\n\x15TransactionStatusMeta\x12<\n\x03\x65rr\x18\x01 \x01(\x0b\x32/.solana.storage.ConfirmedBlock.TransactionError\x12\x0b\n\x03\x66\x65\x65\x18\x02 \x01(\x04\x12\x14\n\x0cpre_balances\x18\x03 \x03(\x04\x12\x15\n\rpost_balances\x18\x04 \x03(\x04\x12L\n\x12inner_instructions\x18\x05 \x03(\x0b\x32\x30.solana.storage.ConfirmedBlock.InnerInstructions\x12\x1f\n\x17inner_instructions_none\x18\n \x01(\x08\x12\x14\n\x0clog_messages\x18\x06 \x03(\t\x12\x19\n\x11log_messages_none\x18\x0b \x01(\x08\x12G\n\x12pre_token_balances\x18\x07 \x03(\x0b\x32+.solana.storage.ConfirmedBlock.TokenBalance\x12H\n\x13post_token_balances\x18\x08 \x03(\x0b\x32+.solana.storage.ConfirmedBlock.TokenBalance\x12\x36\n\x07rewards\x18\t \x03(\x0b\x32%.solana.storage.ConfirmedBlock.Reward\x12!\n\x19loaded_writable_addresses\x18\x0c \x03(\x0c\x12!\n\x19loaded_readonly_addresses\x18\r \x03(\x0c\x12>\n\x0breturn_data\x18\x0e \x01(\x0b\x32).solana.storage.ConfirmedBlock.ReturnData\x12\x18\n\x10return_data_none\x18\x0f \x01(\x08\x12#\n\x16\x63ompute_units_consumed\x18\x10 \x01(\x04H\x00\x88\x01\x01\x42\x19\n\x17_compute_units_consumed\"\x1f\n\x10TransactionError\x12\x0b\n\x03\x65rr\x18\x01 \x01(\x0c\"l\n\x11InnerInstructions\x12\r\n\x05index\x18\x01 \x01(\r\x12H\n\x0cinstructions\x18\x02 \x03(\x0b\x32\x32.solana.storage.ConfirmedBlock.CompiledInstruction\"O\n\x13\x43ompiledInstruction\x12\x18\n\x10program_id_index\x18\x01 \x01(\r\x12\x10\n\x08\x61\x63\x63ounts\x18\x02 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\x9d\x01\n\x0cTokenBalance\x12\x15\n\raccount_index\x18\x01 \x01(\r\x12\x0c\n\x04mint\x18\x02 \x01(\t\x12\x45\n\x0fui_token_amount\x18\x03 \x01(\x0b\x32,.solana.storage.ConfirmedBlock.UiTokenAmount\x12\r\n\x05owner\x18\x04 \x01(\t\x12\x12\n\nprogram_id\x18\x05 \x01(\t\"^\n\rUiTokenAmount\x12\x11\n\tui_amount\x18\x01 \x01(\x01\x12\x10\n\x08\x64\x65\x63imals\x18\x02 \x01(\r\x12\x0e\n\x06\x61mount\x18\x03 \x01(\t\x12\x18\n\x10ui_amount_string\x18\x04 \x01(\t\".\n\nReturnData\x12\x12\n\nprogram_id\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x94\x01\n\x06Reward\x12\x0e\n\x06pubkey\x18\x01 \x01(\t\x12\x10\n\x08lamports\x18\x02 \x01(\x03\x12\x14\n\x0cpost_balance\x18\x03 \x01(\x04\x12>\n\x0breward_type\x18\x04 \x01(\x0e\x32).solana.storage.ConfirmedBlock.RewardType\x12\x12\n\ncommission\x18\x05 \x01(\t\"A\n\x07Rewards\x12\x36\n\x07rewards\x18\x01 \x03(\x0b\x32%.solana.storage.ConfirmedBlock.Reward\"\"\n\rUnixTimestamp\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\"#\n\x0b\x42lockHeight\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x04*I\n\nRewardType\x12\x0f\n\x0bUnspecified\x10\x00\x12\x07\n\x03\x46\x65\x65\x10\x01\x12\x08\n\x04Rent\x10\x02\x12\x0b\n\x07Staking\x10\x03\x12\n\n\x06Voting\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'confirmed_block_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REWARDTYPE._serialized_start=2742
  _REWARDTYPE._serialized_end=2815
  _CONFIRMEDBLOCK._serialized_start=57
  _CONFIRMEDBLOCK._serialized_end=404
  _CONFIRMEDTRANSACTION._serialized_start=407
  _CONFIRMEDTRANSACTION._serialized_end=562
  _TRANSACTION._serialized_start=564
  _TRANSACTION._serialized_end=654
  _MESSAGE._serialized_start=657
  _MESSAGE._serialized_end=958
  _MESSAGEHEADER._serialized_start=960
  _MESSAGEHEADER._serialized_end=1086
  _MESSAGEADDRESSTABLELOOKUP._serialized_start=1088
  _MESSAGEADDRESSTABLELOOKUP._serialized_end=1188
  _TRANSACTIONSTATUSMETA._serialized_start=1191
  _TRANSACTIONSTATUSMETA._serialized_end=1921
  _TRANSACTIONERROR._serialized_start=1923
  _TRANSACTIONERROR._serialized_end=1954
  _INNERINSTRUCTIONS._serialized_start=1956
  _INNERINSTRUCTIONS._serialized_end=2064
  _COMPILEDINSTRUCTION._serialized_start=2066
  _COMPILEDINSTRUCTION._serialized_end=2145
  _TOKENBALANCE._serialized_start=2148
  _TOKENBALANCE._serialized_end=2305
  _UITOKENAMOUNT._serialized_start=2307
  _UITOKENAMOUNT._serialized_end=2401
  _RETURNDATA._serialized_start=2403
  _RETURNDATA._serialized_end=2449
  _REWARD._serialized_start=2452
  _REWARD._serialized_end=2600
  _REWARDS._serialized_start=2602
  _REWARDS._serialized_end=2667
  _UNIXTIMESTAMP._serialized_start=2669
  _UNIXTIMESTAMP._serialized_end=2703
  _BLOCKHEIGHT._serialized_start=2705
  _BLOCKHEIGHT._serialized_end=2740
# @@protoc_insertion_point(module_scope)
