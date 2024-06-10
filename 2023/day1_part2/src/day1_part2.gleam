//// Finds the indexes of numbers in 

import gleam/int
import gleam/io
import gleam/list
import gleam/order.{type Order}
import gleam/result
import gleam/string

pub fn main() {
  let file_content =
    get_list_of_lines(result.unwrap(read_file("./ts_t"), "No file here"))

  let list_of_line_numbers = list.map(file_content, number_in_line)

  io.debug(list.fold(list_of_line_numbers, 0, fn(a, b) { a + b }))
}

fn get_list_of_lines(file_content: String) -> List(String) {
  string.split(file_content, "\n")
}

@external(erlang, "file", "read_file")
fn read_file(path: String) -> Result(a, b)

fn number_in_line(line: String) -> Int {
  let line_as_list = string_to_list(line)

  let digs = find_all_digits(line_as_list, 0, [])
  let str_digs = find_all_string_digits(line_as_list, 0, [])

  let com_list = join_lists(digs, str_digs)

  let num =
    int.undigits(
      [
        result.unwrap(list.first(com_list), 0),
        result.unwrap(list.last(com_list), 0),
      ],
      10,
    )

  case num {
    Ok(num) -> num
    Error(_) -> 0
  }
}

fn compare_index(tuple1: #(Int, Int), tuple2: #(Int, Int)) -> Order {
  let #(index1, _) = tuple1
  let #(index2, _) = tuple2

  case index1 < index2 {
    True -> order.Lt
    False ->
      case index1 == index2 {
        True -> order.Eq
        False -> order.Gt
      }
  }
}

fn return_just_values(inn_list: List(#(Int, Int)), out_list) {
  case inn_list {
    [head, ..tail] -> return_just_values(tail, list.append(out_list, [head.1]))
    [] -> out_list
  }
}

fn join_lists(list1: List(#(Int, Int)), list2: List(#(Int, Int))) -> List(Int) {
  let list_comb = list.append(list1, list2)

  return_just_values(list.sort(list_comb, compare_index), [])
}

fn find_all_digits(
  line: List(String),
  index: Int,
  return_list: List(#(Int, Int)),
) -> List(#(Int, Int)) {
  case line {
    [_, ..] ->
      case int.parse(result.unwrap(list.first(line), "")) {
        Ok(dig) ->
          find_all_digits(
            list.drop(line, 1),
            index + 1,
            list.append(return_list, [#(index, dig)]),
          )
        Error(_) -> find_all_digits(list.drop(line, 1), index + 1, return_list)
      }
    [] -> return_list
  }
}

fn find_all_string_digits(
  line: List(String),
  index: Int,
  return_list: List(#(Int, Int)),
) -> List(#(Int, Int)) {
  case line {
    [_, _, _, ..] ->
      case pars_dig_str_to_int(list.take(line, 5)) {
        Ok(dig) ->
          find_all_string_digits(
            list.drop(line, 1),
            index + 1,
            list.append(return_list, [#(index, dig)]),
          )
        Error(Nil) ->
          case pars_dig_str_to_int(list.take(line, 4)) {
            Ok(dig) ->
              find_all_string_digits(
                list.drop(line, 1),
                index + 1,
                list.append(return_list, [#(index, dig)]),
              )
            Error(Nil) ->
              case pars_dig_str_to_int(list.take(line, 3)) {
                Ok(dig) ->
                  find_all_string_digits(
                    list.drop(line, 1),
                    index + 1,
                    list.append(return_list, [#(index, dig)]),
                  )
                Error(Nil) ->
                  find_all_string_digits(
                    list.drop(line, 1),
                    index + 1,
                    return_list,
                  )
              }
          }
      }
    _ -> return_list
  }
}

fn pars_dig_str_to_int(str: List(String)) -> Result(Int, Nil) {
  let possible_num = list.fold(str, "", fn(a, b) { a <> b })

  case possible_num {
    "one" -> Ok(1)
    "two" -> Ok(2)
    "three" -> Ok(3)
    "four" -> Ok(4)
    "five" -> Ok(5)
    "six" -> Ok(6)
    "seven" -> Ok(7)
    "eight" -> Ok(8)
    "nine" -> Ok(9)
    "zero" -> Ok(0)
    _ -> Error(Nil)
  }
}

fn string_to_list(line: String) -> List(String) {
  string.to_graphemes(line)
}
