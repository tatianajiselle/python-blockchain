#!/usr/bin/env python3
import hashlib
from datetime import datetime

from block import Block


def get_previous_block(blocks):
  return blocks[len(blocks)-1]

def calculateHash(index, previous_hash, timestamp, data): 
  return str(hashlib.sha256(str(index) + previous_hash + str(timestamp) + data))

def create_new_block(index, previous_hash, data):
  date_time = datetime.now()
  my_hash = calculateHash(index + 1, previous_hash, date_time, data )
  return Block(index + 1, my_hash, previous_hash, date_time, data )
  

if __name__ == '__main__':
  genesis = Block(0, '816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7',None , 1465154705, 'my genesis block!!')
  block_chain = [genesis]
  print(block_chain)
  previous_block = get_previous_block(block_chain)
  print(previous_block)
  create_new_block(previous_block.index , previous_block.hash, "data")

  