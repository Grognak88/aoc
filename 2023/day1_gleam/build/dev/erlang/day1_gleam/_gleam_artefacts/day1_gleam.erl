-module(day1_gleam).
-compile([no_auto_import, nowarn_unused_vars, nowarn_unused_function, nowarn_nomatch]).

-export([main/0]).

-spec get_list_of_lines(binary()) -> list(binary()).
get_list_of_lines(File_content) ->
    gleam@string:split(File_content, <<"\n"/utf8>>).

-spec is_digit(binary()) -> boolean().
is_digit(Input) ->
    Is_int = gleam@result:unwrap(gleam@int:parse(Input), -1),
    Is_int > -1.

-spec find_first_digit(list(binary())) -> binary().
find_first_digit(Line) ->
    case Line of
        [Head | Tail] ->
            case is_digit(Head) of
                true ->
                    Head;

                false ->
                    find_first_digit(Tail)
            end;

        _ ->
            <<""/utf8>>
    end.

-spec find_last_digit(list(binary())) -> binary().
find_last_digit(Line) ->
    find_first_digit(lists:reverse(Line)).

-spec string_to_list(binary(), list(binary())) -> list(binary()).
string_to_list(Line, Accumalator) ->
    case gleam@string:first(Line) of
        {ok, Char} ->
            string_to_list(
                gleam@string:drop_left(Line, 1),
                lists:append(Accumalator, [Char])
            );

        {error, _} ->
            Accumalator
    end.

-spec number_in_line(binary()) -> integer().
number_in_line(Line) ->
    First_dig = find_first_digit(string_to_list(Line, [])),
    Last_dig = find_last_digit(string_to_list(Line, [])),
    case gleam@int:parse(<<First_dig/binary, Last_dig/binary>>) of
        {ok, Num} ->
            Num;

        {error, _} ->
            -1
    end.

-spec main() -> integer().
main() ->
    File_content = get_list_of_lines(
        gleam@result:unwrap(
            file:read_file(<<"./ts_t"/utf8>>),
            <<"No file here"/utf8>>
        )
    ),
    List_of_line_numbers = gleam@list:map(File_content, fun number_in_line/1),
    gleam@io:debug(
        gleam@list:fold(List_of_line_numbers, 0, fun(A, B) -> A + B end)
    ).
